import pytest

from gymanager.app import create_app


@pytest.fixture(scope="module")
def app():
    """
    Build an app instance to be used during tests.
    """

    return create_app()
