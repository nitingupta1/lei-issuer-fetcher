import asyncio
import time
from app.service import LeiIssuerService
import aiohttp
def test_concurrent_fetch_is_faster():
    async def run_test():
        service = LeiIssuerService(ttl=5)

        start = time.time()
        # sequential fetch
        async with aiohttp.ClientSession() as session:
            lei_issuers1 = await service.fetch_lei_issuers_page(session,page=1, page_size=5)
            lei_issuers2 = await service.fetch_lei_issuers_page(session,page=2, page_size=5)
        sequential_duration = time.time() - start
        start = time.time()
        
        # concurrent fetch
        results = await service.fetch_lei_issuers_multiple_pages([1, 2], page_size=5)
        concurrent_duration = time.time() - start

        # Both results should have LEI Issuers
        assert len(lei_issuers1) > 0
        assert len(lei_issuers2) > 0
        assert len(results[1]) > 0
        assert len(results[2]) > 0

        # Concurrency should not be slower than sequential
        assert concurrent_duration <= sequential_duration

    asyncio.run(run_test())