import requests
import schemas

from fastapi import FastAPI

app = FastAPI()


@app.get("/{coin}")
async def main(coin: str):
    return requests.get(f'https://api.coingecko.com/api/v3//coins/list').json()
