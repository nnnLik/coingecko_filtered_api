import requests

from schemas import Converter
from fastapi import FastAPI
from pydantic import ValidationError

app = FastAPI()


@app.get("/{coin}")
async def test_model(coin: str):
    user_coin = requests.get(f'https://api.coingecko.com/api/v3//coins/{coin}').json()
    try:
        output = Converter(**user_coin)
    except ValidationError as error:
        print(error.json())
    else:
        return output


@app.get("/about_coin/{coin}")
async def about_coin(coin: str):
    get_about_coin = requests.get(f'https://api.coingecko.com/api/v3//coins/{coin}').json()
    return get_about_coin


@app.get("/list/get_list")
async def list_of_coins():
    get_list_of_coins = requests.get(f'https://api.coingecko.com/api/v3/coins/list').json()
    return get_list_of_coins
