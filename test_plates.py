import plates
import pytest

def test_valid_plate():
    assert plates.is_valid("AB123") == True

def test_invalid_plate_too_short():
    assert plates.is_valid("A1") == False

def test_invalid_plate_too_long():
    assert plates.is_valid("ABCDE1234") == False

def test_invalid_plate_first_two_digits_not_letters():
    assert plates.is_valid("12345A") == False

def test_invalid_plate_last_digit_not_letter_or_nonzero_number():
    assert plates.is_valid("AB012") == False

def test_invalid_plate_zero_placement():
    assert plates.is_valid("AB0C1") == False

def test_invalid_plate_contains_special_characters():
    assert plates.is_valid("AB@12") == False
