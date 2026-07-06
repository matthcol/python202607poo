import pytest

from movie import Movie


def test_movie_duration_hour_minute_when_has_duration():
    # given
    m = Movie("E.T. the Extra-Terrestrial", 1982, 115)
    # when
    h_m = m.duration_hour_minute()
    # then
    assert h_m is not None, "has a result"
    assert h_m == (1, 55), "hour and minute ok"

def test_movie_duration_hour_minute_when_has_no_duration():
    # given
    m = Movie("E.T. the Extra-Terrestrial", 1982)
    # when
    h_m = m.duration_hour_minute()
    # then
    assert h_m is None, "has no result"

@pytest.mark.parametrize(
        "item",
        [
            "E.T. the Extra-Terrestrial",
            "E.T.",
            "Extra",
            "Terrestrial",
            "e.t. the extra-terrestrial",
            "e.T.",
            "eXtRa",
            "tErResTriAl",
        ],
        ids=[
            "whole title CS",
            "start of title CS",
            "middle of title CS",
            "end of title CS",
            "whole title CI",
            "start of title CI",
            "middle of title CI",
            "end of title CI",
        ]
)
def test_movie_contains_when_found(movie_et: Movie, item):
    # when
    result = item in movie_et
    # then
    assert result, "contains ok"

@pytest.mark.parametrize(
        "item",
        [
            "Terminator",
            "ET",
            123,
            None,
            True,
            ("E.T.", "Extra", "Terrestrial"),
        ],
        ids=[
            "text not ...",
            "text not ...",
            "a number",
            "None",
            "a boolean",
            "a tuple"
        ]
)
def test_movie_contains_when_not_found(movie_et: Movie, item):
    # when
    result = item in movie_et
    # then
    assert not result, "contains ko"