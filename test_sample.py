import pytest

from sample import add, raise_zero_division_error, multiply_even_number

# def test_add():
#     assert add(1, 2) == 3

@pytest.mark.parametrize(
    "input,expected", 
    [({"x": 1, "y": 2}, 3), ({"x": 10, "y": 5}, 15)]
)
def test_add(input, expected):
    assert add(input["x"], input["y"]) == expected

# def test_multiply_even_number():
#     assert multiply_even_number(2) == 4

@pytest.mark.parametrize("input, expected", [(2, 4), (1, 1)])
def test_multiply_even_number(input, expected):
    assert multiply_even_number(input) == expected

def test_raise_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        raise_zero_division_error()