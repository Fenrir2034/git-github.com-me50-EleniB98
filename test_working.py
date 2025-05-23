from working import convert


def test_valid_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_invalid_time():
    try:
        convert("9:60 AM to 5:60 PM")
        assert False  # The line should not be reached
    except ValueError:
        assert True

    try:
        convert("9 AM - 5 PM")
        assert False  # The line should not be reached
    except ValueError:
        assert True

    try:
        convert("09:00 AM - 17:00 PM")
        assert False  # The line should not be reached
    except ValueError:
        assert True
