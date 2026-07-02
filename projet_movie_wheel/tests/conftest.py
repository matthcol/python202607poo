import pytest

from movie import Mo_vie


@pytest.fixture
def movie_et() -> Mo_vie:
    return Mo_vie(title="E.T. the Extra-Terrestrial", year=1982, duration=115)