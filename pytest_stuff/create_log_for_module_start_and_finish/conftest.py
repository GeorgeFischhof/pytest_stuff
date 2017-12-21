
import logging

import pytest

from testlib.budapest import log_messages


@pytest.fixture(scope='module', autouse=True)
def setup_and_teardown_module(request):
    module_name = request.module.__name__
    logging.info(log_messages.start_execution(module_name))
    yield
    logging.info(log_messages.finish_execution(module_name))
