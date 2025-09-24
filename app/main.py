from fastapi import FastAPI, Query
from typing import List, Dict
from app.service import LeiIssuerService
from app.dto import LeiIssuerDto
import aiohttp
app = FastAPI(title=" LEI Issuer Fetcher Service")
service = LeiIssuerService(ttl=60)

@app.get("/issuers", response_model=List[LeiIssuerDto])
async def get_lei_issuers(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1, le=100)):
    async with aiohttp.ClientSession() as session:
        return await service.fetch_lei_issuers_page(session=session, page=page, page_size=page_size)

@app.get("/issuers/multipage", response_model=Dict[int, List[LeiIssuerDto]])
async def get_lei_issuers_multipage(pages: str = Query(...), page_size: int = Query(10, ge=1, le=100)):
    page_list = [int(p.strip()) for p in pages.split(",")]
    return await service.fetch_lei_issuers_multiple_pages(page_list, page_size)