from pydantic import BaseModel
class LeiIssuerDto(BaseModel):
    lei: str = None
    name: str = None
    marketingName: str = None
    website: str = None
    accreditationDate: str = None