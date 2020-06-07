import pytest
from aioresponses import aioresponses

from site_connectivity_checker.adapters.request_performer import RequestPerformer
from site_connectivity_checker.adapters.request_performer.exceptions import (
    ConnectionException,
)


@pytest.fixture
def test_url():
    return "http://www.google.com"


@pytest.fixture
def timeout_test_url():
    return "http://www.not-exist.not-exits"


def test_instance():
    assert isinstance(RequestPerformer(), RequestPerformer)


@pytest.mark.asyncio
async def test_perform_request(test_url):
    expected_status = 300
    with aioresponses() as m:
        m.get(test_url, payload=dict(foo="bar"), status=expected_status)
        result = await RequestPerformer().perform_request(url=test_url)
        assert result == expected_status


@pytest.mark.asyncio
@pytest.mark.integration
async def test_perform_real_request_timeout(timeout_test_url):
    result = None
    with pytest.raises(ConnectionException):
        result = await RequestPerformer().perform_request(url=timeout_test_url)
    assert result != 200
