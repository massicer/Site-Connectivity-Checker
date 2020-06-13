import time
import logging, coloredlogs
import asyncio

from pytime_converter.service.convert_service import get_milliseconds_value_for_input
import click

from .checker import Checker
from site_connectivity_checker.adapters.request_performer import RequestPerformer
from .checker.entities import endpoint, rule
from site_connectivity_checker.services.checker.entities.exceptions import (
    ServiceNotAvailableException,
)


def setup_logging():
    logging.basicConfig(level=logging.DEBUG)
    coloredlogs.install(level="DEBUG")


@click.command()
@click.option("--number_of_request", help="Number of request.")
@click.option("--url_protocol", prompt="The url protocol")
@click.option("--service_port", prompt="The service port")
@click.option("--service_url", prompt="The service url")
@click.option("--check_time", prompt="How often to check the availability")
def run_service(
    number_of_request: int,
    url_protocol: str,
    service_port: str,
    service_url: str,
    check_time: str,
):

    setup_logging()

    end = endpoint.Endpoint(protocol=url_protocol, url=service_url, port=service_port)

    milliseconds = get_milliseconds_value_for_input(check_time)

    rul = rule.AvailabilityRule(
        request_to_perform=number_of_request, interval_in_milliseconds=milliseconds
    )

    asyncio.run(run(endpoint=end, rule=rul))


async def run(endpoint: endpoint.Endpoint, rule: rule.AvailabilityRule):

    logging.info("Service started")
    checker = Checker(logger=logging, request_performer=RequestPerformer())

    number_of_checks = 0
    number_of_failed_checks = 0
    number_of_successful_checks = 0
    while 1:
        number_of_checks += 1
        logging.info(f"Preparing to perform check # {number_of_checks}")

        try:
            await checker.perform_requests(endpoint=endpoint, rule=rule)
        except ServiceNotAvailableException:
            number_of_failed_checks += 1
            logging.info(f"Check  #{number_of_checks} failed")
        else:
            number_of_successful_checks += 1
            logging.info(f"Check  #{number_of_checks} successfull")
        number_of_checks += 1

        time.sleep(rule.interval_in_milliseconds / 1000)
        logging.info(
            f"""Current stats:"""
            f"""'Number of total checks: {number_of_checks}"""
            f"""Number of failed checks: {number_of_failed_checks}"""
            f"""Number of failed checks: {number_of_successful_checks}"""
        )
