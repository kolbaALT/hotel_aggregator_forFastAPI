from pydantic import BaseModel, Field


class Hotel(BaseModel):
    title: str
    stars: int

class HotelPATCH(BaseModel):
    title: str | None = Field(None)
    stars: int | None = Field(None)