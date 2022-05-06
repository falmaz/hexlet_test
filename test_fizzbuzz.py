import pytest
from fizzbuzz import fizz_buzz

data = [
        (1, "Number: 1"),
        (3, "Fizz!"),
        (5, "Buzz!"),
        (15, "FizzBuzz!"),
        ]
@pytest.mark.parametrize(
        "num, expected",
        data
        )
def test_fizz_buzz(num, expected):
    assert fizz_buzz(num) == expected

