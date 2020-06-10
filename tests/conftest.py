import pytest


@pytest.fixture
def async_logger(mocker):
    return mocker.MagicMock(id="async logger")
