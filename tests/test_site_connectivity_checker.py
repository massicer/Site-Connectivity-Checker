import re
import pytest

from site_connectivity_checker import __version__


@pytest.fixture
def allowed_regex_version():
    return "[0-9].[0-9].[0-9]"


def test_version_allowed(allowed_regex_version):
    assert __version__ is not None
    assert re.match(allowed_regex_version, __version__)
