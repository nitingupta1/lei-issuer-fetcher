import aiohttp
import asyncio
from typing import List, Dict
from app.cache import MemoryCache
from app.dto import LeiIssuerDto
from pydantic import ValidationError

class LeiIssuerService:
    BASE_ENDPOINT = "https://api.gleif.org/api/v1/lei-issuers"

    def __init__(self, ttl: int = 60):
        self.cache = MemoryCache(ttl=ttl)

    ##Fetch Lei issuers for one page
    async def fetch_lei_issuers_page(self, session: aiohttp.ClientSession, page: int, page_size: int) -> List[LeiIssuerDto]:
        cached = self.cache.get(page=page, page_size=page_size)
        if cached:
            return cached

        url = f"{self.BASE_ENDPOINT}?page%5Bnumber%5D={page}&page%5Bsize%5D={page_size}"
        try:
            async with session.get(url) as response:
                if response.status != 200:
                    ## placeholder to handle and return the error code if needed.
                    return []
                json_data = await response.json()
                try:
                    lei_issuers = []
                    for lei_issuer in json_data.get("data", []):                
                        lei_issuer_attributes = lei_issuer["attributes"]
                        lei_issuers.append(LeiIssuerDto(**lei_issuer_attributes))                        
                except ValidationError as e:
                    return []
                self.cache.set(lei_issuers, page=page, page_size=page_size)
                return lei_issuers
        except aiohttp.ClientError as e:
            ## placeholder to handle and return the error if needed.
            return []

    ##Fetch Lei issuers for multiple pages
    async def fetch_lei_issuers_multiple_pages(self, pages: List[int], page_size: int) -> Dict[int, List[LeiIssuerDto]]:
        async with aiohttp.ClientSession() as session:
            tasks = [
                self.fetch_lei_issuers_page(session, page, page_size)
                for page in pages
            ]
            results = await asyncio.gather(*tasks)
            return {page: result for page, result in zip(pages, results)}