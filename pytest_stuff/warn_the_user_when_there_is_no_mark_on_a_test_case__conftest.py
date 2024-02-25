# warn the user when there is no mark on a test case

# conftest.py

import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        markers = list(item.iter_markers())
        if not markers:
            print(f"item {item.nodeid} does not have any marks set")
            item.add_marker(pytest.mark.skip(reason=f"item {item.nodeid} does not have any marks set"))
