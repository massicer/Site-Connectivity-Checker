from site_connectivity_checker.services.checker.entities.exceptions import (
    ServiceNotAvailableException,
)


def is_status_code_response_successful(status_code: int) -> bool:
    if status_code is not None and status_code >= 200 and status_code < 300:
        return True
    raise ServiceNotAvailableException(
        f"Status code {status_code} means service not available"
    )
