import random
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI

app = FastAPI(title="Mock Bitcoin Sentiment API")


def generate_entry(offset_seconds: int):
    now = datetime.now(tz=timezone.utc)
    ts = now - timedelta(seconds=offset_seconds)

    mean = round(random.uniform(-0.8, 0.8), 2)
    count = random.randint(2000, 12000)

    return {
        "count": count,
        "timestamp": ts.timestamp(),
        "rate": round(random.uniform(-0.05, 0.05), 2),
        "last": round(random.uniform(-0.8, 0.8), 2),
        "sum": round(mean * count, 2),
        "mean": mean,
        "median": round(random.uniform(-0.8, 0.8), 2),
        "btc_price": round(random.uniform(65000, 110000), 0),
    }


@app.get("/v1/bitcoin.json")
async def get_bitcoin_data():
    return [generate_entry(i * 30) for i in range(40, -1, -1)]