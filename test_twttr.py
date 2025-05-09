import pytest
from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"

def test_shorten_with_vowels():
    assert shorten("AEIOUaeiou") == ""
    assert shorten("python") == "pythn"

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_all_vowels():
    assert shorten("AEIOUaeiou") == ""

def test_shorten_mixed_case():
    assert shorten("HeLLo") == "HLL"
    assert shorten("WOrLD") == "WrLD"

def test_shorten_with_numbers():
    assert shorten("hello123") == "hll123"
    assert shorten("123world") == "123wrld"

def test_shorten_with_punctuation():
    assert shorten("hello!@#") == "hll!@#"
    assert shorten("!@#world") == "!@#wrld"

if __name__ == "__main__":
    pytest.main()


