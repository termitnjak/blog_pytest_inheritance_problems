import pytest


@pytest.fixture
def Human():
    from humans.human import Human
    return Human


@pytest.fixture
def human(Human):
    return Human()
