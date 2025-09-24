import asyncio
from app.service import LeiIssuerService
import aiohttp
def test_fetch_lei_issuers_real_api():
    async def run_test():
        service = LeiIssuerService(ttl=5)
        async with aiohttp.ClientSession() as session:
            lei_issuers = await service.fetch_lei_issuers_page(session,page=1, page_size=5)
            assert len(lei_issuers) > 0
            lei_issuer = lei_issuers[0]
            assert hasattr(lei_issuer, "lei")
            assert hasattr(lei_issuer, "name")
            assert hasattr(lei_issuer, "marketingName")
            assert hasattr(lei_issuer, "website")

    asyncio.run(run_test())

def test_fetch_lei_issuers_multiple_pages_real_api():
    async def run_test():
        service = LeiIssuerService(ttl=5)
        results = await service.fetch_lei_issuers_multiple_pages([1, 2], page_size=3)
        assert len(results[1]) > 0
        assert len(results[2]) > 0

    asyncio.run(run_test())