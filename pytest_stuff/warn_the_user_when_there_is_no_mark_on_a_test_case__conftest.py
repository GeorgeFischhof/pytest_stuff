# warn the user when there is no mark on a test case

# conftest.py

import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        markers = list(item.iter_markers())
        if not markers:
            # pytest.fail(f"item {item.nodeid} does not have any marks set")
            # pytest.skip(f"item {item.nodeid} does not have any marks set")
            # raise pytest.PytestCollectionWarning(f"item {item.nodeid} does not have any marks set")
            # raise pytest.PytestUnknownMarkWarning(f"item {item.nodeid} does not have any marks set")
            # raise pytest.PytestWarning(f"item {item.nodeid} does not have any marks set")
            print(f"item {item.nodeid} does not have any marks set")
            item.add_marker(pytest.mark.skip(reason=f"item {item.nodeid} does not have any marks set"))
