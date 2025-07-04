from string_calculator import add
import pytest
def test_empty_string_returns_zero() :
    assert add("") == 0

def test_single_number_return_values() :
    assert add("1") == 1

def test_two_number_returns_sum() :
    assert add("1,2") == 3

def test_multiple_numbers_returns_sum() :
    assert add("1,3,4,7") == 15

def test_newline_and_comma_delimiters() :
    assert add("1\n2,3") == 6

def test_custom_delimiter() :
    assert add("//;\n;1;2") == 3

def test_negative_numbers_throw_exception() :
    with pytest.raises(Exception) as excinfo :
        add("1,-5,-9")
    assert "negative numbers not allowed -5,-9" in str(excinfo.value)

def test_ignore_numbers_greater_than_1000():
    assert add("2,1001") == 2
    assert add("2,1000") == 1002