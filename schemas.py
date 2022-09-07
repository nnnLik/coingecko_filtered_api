from pydantic import BaseModel
from typing import Union


class Converter(BaseModel):
    id: str
    symbol: Union[str, None]
    name: Union[str, None]
    asset_platform_id: Union[str, None]
    platforms: Union[str, None]
    detail_platforms: Union[str, None]
    block_time_in_minutes: Union[str, None]
    hashing_algorithm: Union[str, None]
    categories: Union[str, None]
    public_notice: Union[str, None]
    additional_notices: Union[str, None]
    localization: Union[str, None]
    description: Union[str, None]
    links: Union[str, None]
    image: Union[str, None]
    country_origin: Union[str, None]
    genesis_date: Union[str, None]
    sentiment_votes_up_percentage: Union[str, None]
    sentiment_votes_down_percentage: Union[str, None]
    market_cap_rank: Union[str, None]
    coingecko_rank: Union[str, None]
    coingecko_score: Union[str, None]
    developer_score: Union[str, None]
    community_score: Union[str, None]
    liquidity_score: Union[str, None]
    public_interest_score: Union[str, None]
    market_data: Union[str, None]
    community_data: Union[str, None]
    developer_data: Union[str, None]
    public_interest_stats: Union[str, None]
    status_updates: Union[str, None]
    last_updated: Union[str, None]
    tickers: Union[str, None]

