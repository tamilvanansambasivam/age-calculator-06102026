from age_tools import make_greeting, calculate_age, year_turning


def test_greeting():
    assert make_greeting("Tamil") == "Hello, Tamil!"


def test_calculate_age():
    assert calculate_age(2000, 2026) == 26


def test_year_turning_100():
    assert year_turning(100, 2000) == 2100