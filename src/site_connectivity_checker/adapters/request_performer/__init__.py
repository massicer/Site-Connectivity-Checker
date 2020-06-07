import aiohttp

from .exceptions import ConnectionException


class RequestPerformer:
    def __init__(self):
        self.shared_session = None

    async def perform_request(self, url: str, timeout: int = 60) -> int:
        if self.shared_session is None:
            self.shared_session = aiohttp.ClientSession()
        try:
            async with self.shared_session.get(url=url, timeout=timeout) as response:
                return response.status
        except aiohttp.client_exceptions.ClientConnectorError as e:
            raise ConnectionException(e)
        finally:
            await self.shared_session.close()
