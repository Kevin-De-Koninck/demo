import logging
import pytest
from .context import Demo


LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope='function')
def demo_object():
    LOGGER.info("Initializing the module and returning the object...")
    yield Demo()
    LOGGER.info("Breaking down the module.")
    # Do clean up here

