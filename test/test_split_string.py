import pytest

from lyfttechnicalsample.split_string import split_string


def test_split_string_returns_empty_string_for_empty_string():
    assert '' == split_string('')


def test_split_string_returns_empty_string_for_string_length_one():
    assert '' == split_string('a')


def test_split_string_raises_type_error_exception_for_none():
    with pytest.raises(TypeError):
        split_string(None)


def test_split_string_returns_last_character_for_string_length_three():
    assert 'c' == split_string('sbc')


def test_split_string_returns_two_charcters_for_string_length_seven():
    assert 'cf' == split_string('abcdefg')
