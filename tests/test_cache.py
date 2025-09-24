import time
from app.cache import MemoryCache

def test_cache_set_and_get():
    cache = MemoryCache(ttl=5)
    cache.set(["lei_issuer1"], 1, 10)
    assert cache.get(1, 10) == ["lei_issuer1"]

def test_cache_expiry():
    cache = MemoryCache(ttl=1)
    cache.set(["lei_issuer1"], 1, 10)
    time.sleep(2)
    assert cache.get(1, 10) is None