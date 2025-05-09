from um import count


def test_um_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_um_no_count():
    assert count("yummy") == 0
    assert count("brum") == 0
    assert count("lump") == 0
