from pydantic import BaseModel, Field
from typing import Union
from datetime import date

class Converter(BaseModel):
    name: str
    categories: list
    creation_date: date = Field(alias='genesis_date')
    coin_rank: int = Field(alias='coingecko_rank')
    links: dict


