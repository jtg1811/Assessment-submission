from string_calculator import add

def test_empty_string_returns_zero() :
    assert add("") == 0

def test_single_number_return_values() :
    assert add("1") == 1

def test_two_number_returns_sum() :
    assert add("1,2") == 3
    