from pydantic import BaseModel


class Converter(BaseModel):
    coin: str = ' '
    Description: str = ' '
    to_EUR: float
    to_USD: float
    to_BYN: float
