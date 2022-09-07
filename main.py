import requests
from schemas import Converter
from fastapi import FastAPI


app = FastAPI()

a = {'id': 'qwe', 'symbol': 'qwewee', 'snt_new': 123}


@app.get("/{coin}")
async def test_model(coin: str):
    user_coin = requests.get(f'https://api.coingecko.com/api/v3//coins/{coin}').json()
    output = Converter(**user_coin)
    return output


@app.get("/about_coin/{coin}")
async def about_coin(coin: str):
    user_coin = requests.get(f'https://api.coingecko.com/api/v3//coins/{coin}').json()
    return user_coin


@app.get("/list_of_coins")
async def list_of_coins():
    user_coin = requests.get(f'https://api.coingecko.com/api/v3//coins/list').json()
    return user_coin
