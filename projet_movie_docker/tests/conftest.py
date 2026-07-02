import pytest

from movie import Movie


@pytest.fixture
def movie_et() -> Movie:
    return Movie(title="E.T. the Extra-Terrestrial", year=1982, duration=115)