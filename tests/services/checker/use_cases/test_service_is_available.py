import pytest
from functools import partial

from site_connectivity_checker.services.checker.use_cases.service_is_available import (
    is_status_code_response_successful,
)
from site_connectivity_checker.services.checker.entities.exceptions import (
    ServiceNotAvailableException,
)


@pytest.mark.parametrize(
    "status_code, allowed",
    [(200, True), (201, True), (299, True), (300, False), (400, False), (500, False)],
)
def test_is_status_code_response_successful(status_code, allowed):
    trigger = partial(is_status_code_response_successful, status_code=status_code)

    if allowed:
        assert trigger()
    else:
        with pytest.raises(ServiceNotAvailableException):
            trigger()
