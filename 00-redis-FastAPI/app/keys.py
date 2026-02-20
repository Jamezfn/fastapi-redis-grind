from app.decorators import prefixed_key
from app.config import settings

class Keys:
    """ Methods to generate key names for Redis data structures. """
    def __init__(self, prefix: str = settings.key_prefix):
        self.prefix = prefix

    @prefixed_key
    def timeseries_sentiment_key(self) -> str:
        """A time series containing 30-second snapshots of BTC sentiment.
        """
        return 'sentiment:mean:30s'
    
    @prefixed_key
    def timeseries_price_key(self) -> str:
        """A time series containing 30-second snapshots of BTC price.
        """
        return 'price:mean:30s'
    
    @prefixed_key
    def cache_key(self) -> str:
        return 'cache'