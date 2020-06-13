import aiohttp

from .exceptions import ConnectionException


class RequestPerformer:
    async def perform_request(self, url: str, timeout: int = 1) -> int:
        shared_session = aiohttp.ClientSession()
        try:
            async with shared_session.get(url=url, timeout=timeout) as response:
                return response.status
        except aiohttp.client_exceptions.ClientConnectorError as e:
            raise ConnectionException(e)
        finally:
            await shared_session.close()
