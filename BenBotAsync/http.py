import aiohttp
from typing import Any, Dict


class HTTPClient:
    def __init__(self, connector=None) -> None:
        self.connector = connector
        self.BEN_BOT_BASE = 'https://benbot.app/api/v1'

    async def request(self, url: str, method: str = 'GET', params: dict = None, **kwargs: Any) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.request(
                    method=method,
                    url=f'{self.BEN_BOT_BASE}{url}',
                    params=params,
                    **kwargs
            ) as request:
                return await request.json()
