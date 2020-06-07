from typing import Any

from pydantic import BaseModel
import asyncio

from .entities import endpoint, rule
from site_connectivity_checker.adapters.request_performer import RequestPerformer
from site_connectivity_checker.services.checker.use_cases import service_is_available


class Checker:
    logger: Any
    request_performer: RequestPerformer

    def __init__(self, logger: Any, request_performer: RequestPerformer):
        self.logger = logger
        self.request_performer = request_performer

    class Config:
        arbitrary_types_allowed = True

    async def perform_requests(
        self, endpoint: endpoint.Endpoint, rule: rule.AvailabilityRule
    ):
        """
        Perform all the request and raises ServiceNotAvailableException if
        the service is not available.
        """
        self.logger.info(
            f"Preparing to perform {rule.request_to_perform} request to url {endpoint.compose_url()}"
            f"Every {rule.interval_in_milliseconds} milliseconds"
        )

        tasks = [
            self.request_performer.perform_request(url=endpoint.compose_url())
            for i in range(0, rule.request_to_perform)
        ]
        results = await asyncio.gather(*tasks, return_exceptions=False)

        for i in results:
            service_is_available.is_status_code_response_successful(status_code=i)
