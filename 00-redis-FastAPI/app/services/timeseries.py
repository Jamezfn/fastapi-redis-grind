from typing import List, Dict, Union, Iterable, Tuple
from datetime import datetime, timezone

from app.keys import Keys
from app.config import settings
from app.utils.utils import get_direction

BitcoinSentiments = List[Dict[str, Union[str, float]]]

async def add_many_to_timeseries(redis, key_pairs: Iterable[Tuple[str, str]], data: BitcoinSentiments):
    args = ["TS.MADD"]
    for datapoint in data:
        timestamp = int(float(datapoint["timestamp"] * 1000))
        for ts_key, sample_key in key_pairs:
            args.extend([ts_key, timestamp, datapoint[sample_key]])

    return await redis.execute_command(*args)

async def create_timeseries_keys(redis, keys: Keys) -> None:
    ts_sentiment_key = keys.timeseries_sentiment_key()
    ts_price_key = keys.timeseries_price_key()

    for key in [ts_sentiment_key, ts_price_key]:
        try:
            await redis.execute_command("TS.CREATE", key, "DUPLICATE_POLICY", "LAST")
        except Exception as e:
            if "already exists" in str(e).lower():
                pass 
            else:
                raise

async def persist(redis, keys: Keys, data: BitcoinSentiments) -> None:
    await create_timeseries_keys(redis, keys)

    ts_sentiment_key = keys.timeseries_sentiment_key()
    ts_price_key = keys.timeseries_price_key()

    await add_many_to_timeseries(
        redis,
        (
            (ts_price_key, "btc_price"),
            (ts_sentiment_key, "mean"),
        ),
        data
    )

async def get_latest_timestamp(redis, ts_key):
    return await redis.execute_command("TS.GET", ts_key)

async def get_hourly_average(redis, ts_key: str, from_timestamp: int):
    return await redis.execute_command('TS.RANGE', ts_key, from_timestamp, "+", "AGGREGATION", "avg", settings.hourly_bucket)

async def calculate_three_hours_of_data(redis, keys: Keys):
    sentiment_key = keys.timeseries_sentiment_key()
    price_key = keys.timeseries_price_key()

    latest = await get_latest_timestamp(redis, sentiment_key)

    three_hours_ago = latest[0] - (1000 * 60 * 60 * 3)
    sentiment = await get_hourly_average(redis, sentiment_key, three_hours_ago)
    price = await get_hourly_average(redis, price_key, three_hours_ago)

    last_three_hours = [
        {
            "price": p[1],
            "sentiment": s[1],
            "time": datetime.fromtimestamp(p[0] / 1000, tz=timezone.utc),
        }
        for p, s in zip(price, sentiment)
    ]

    return {
        "hourly_average_of_averages": last_three_hours,
        "sentiment_direction": get_direction(last_three_hours, "sentiment"),
        "price_direction": get_direction(last_three_hours, "price"),
    }