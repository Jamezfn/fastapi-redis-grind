from typing import List, Dict, Union

from app.keys import Keys

BitcoinSentiments = List[Dict[str, Union[str, float]]]

async def persist(redis, keys: Keys, data: BitcoinSentiments) -> None:
    ts_sentiment_key = keys.timeseries_sentiment_key()
    ts_price_key = keys.timeseries_price_key()
    pass