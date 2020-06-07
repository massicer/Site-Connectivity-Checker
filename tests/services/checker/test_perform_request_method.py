from functools import partial
import asynctest

import pytest
from unittest.mock import patch, call

from site_connectivity_checker.services.checker import Checker
from site_connectivity_checker.services.checker.entities.exceptions import (
    ServiceNotAvailableException,
)


@pytest.mark.asyncio
@pytest.mark.parametrize("number_of_requests", [1])
@pytest.mark.parametrize("requests_valid", [True])
@asynctest.patch(
    """site_connectivity_checker.services.checker.use_cases.service_is_available."""
    """is_status_code_response_successful"""
)
async def test_perform_request(
    is_status_code_response_successful,
    async_checker,
    mocker,
    number_of_requests,
    requests_valid,
):
    assert isinstance(async_checker, Checker)

    composed_url = mocker.MagicMock(id="composed_url")
    endpoint = mocker.MagicMock(id="endpoint")
    endpoint.composed_url.return_value = composed_url

    rule = mocker.MagicMock(id="rule")
    rule.request_to_perform = number_of_requests

    async def trigger():
        await async_checker.perform_requests(endpoint=endpoint, rule=rule)

    returns_values = [mocker.MagicMock() for i in range(0, 100)]
    async_checker.request_performer.perform_request.side_effect = returns_values

    if requests_valid:
        is_status_code_response_successful.return_value = True
        await trigger()
        is_status_code_response_successful.assert_called()
    else:
        status_ok.side_effect = ServiceNotAvailableException
        with pytest.raises(ServiceNotAvailableException):
            await trigger()
        is_status_code_response_successful.assert_called()

    calls = [call(url=endpoint.compose_url()) for i in range(0, number_of_requests)]

    async_checker.request_performer.perform_request(url="random").assert_has_calls(
        calls
    )
