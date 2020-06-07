import asyncio

import pytest

from site_connectivity_checker.services.checker import Checker


@pytest.fixture
async def mocked_request_performer(mocker):
    async def return_async_value(url):
        return mocker.MagicMock(id="return async value")

    req_performer = mocker.MagicMock(id="async request performer")
    req_performer.perform_request = return_async_value
    return req_performer


@pytest.fixture
async def async_checker(async_logger, mocked_request_performer):
    return Checker(logger=async_logger, request_performer=mocked_request_performer)
