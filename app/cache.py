import time

class MemoryCache:
    def __init__(self, ttl=60):
        self.ttl = ttl
        self.store = {}

    def get(self, page, page_size):
        key = (page, page_size)
        if key in self.store:
            timestamp, value = self.store[key]
            if time.time() - timestamp < self.ttl:
                return value
        return None

    def set(self, value, page, page_size):
        key = (page, page_size)
        self.store[key] = (time.time(), value)
