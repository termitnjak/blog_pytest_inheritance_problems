import pytest

from humans.conftest import human


@pytest.fixture
def Human():
    from .president import President
    return President
