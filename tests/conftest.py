import pytest

from movie import Movie


@pytest.fixture
def movie_et() -> Movie:
    return Movie("E.T. the Extra-Terrestrial", 1982, 115)