from datetime import date
import pytest
from seasons import calculate_age_in_minutes, print_age_in_words, get_user_birthdate

def test_calculate_age_in_minutes():
    # Test 1: Age one year ago
    birthdate = "2000-01-01"
    age_in_minutes = calculate_age_in_minutes(birthdate)
    assert age_in_minutes == 525600  # 365 days * 24 hours * 60 minutes

    # Test 2: Age two years ago
    birthdate = "1999-01-01"
    age_in_minutes = calculate_age_in_minutes(birthdate)
    assert age_in_minutes == 1051200  # 2 * 525600

def test_print_age_in_words(capfd):
    # Test 1: Print age in words for 525600 minutes
    print_age_in_words(525600)
    captured = capfd.readouterr()
    assert captured.out.strip() == "Five hundred twenty-five thousand, six hundred"

    # Test 2: Print age in words for 1051200 minutes
    print_age_in_words(1051200)
    captured = capfd.readouterr()
    assert captured.out.strip() == "One million, fifty-one thousand, two hundred"

def test_get_user_birthdate(monkeypatch):
    # Test 1: Valid birthdate
    monkeypatch.setattr('builtins.input', lambda _: '1990-05-15\n')
    assert get_user_birthdate() == "1990-05-15"

    # Test 2: Invalid birthdate format
    monkeypatch.setattr('builtins.input', lambda _: 'invalid_date\n')
    with pytest.raises(SystemExit) as excinfo:
        get_user_birthdate()
    assert excinfo.value.code == 1

