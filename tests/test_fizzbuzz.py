import pytest
from lambda_handler.fizzbuzz import FizzBuzz


class TestFizzBuzz:
    @pytest.fixture(
        params=[
            # input, expected
            (1, "1"),
            (2, "2"),
            (3, "Fizz"),
            (4, "4"),
            (5, "Buzz"),
            (9, "Fizz"),
            (10, "Buzz"),
            (15, "FizzBuzz"),
            (30, "FizzBuzz"),
        ]
    )
    def case__print(self, request) -> tuple[int, str]:
        return request.param

    def test_fizzbuzz(self, case__print):
        fizzbuzz = FizzBuzz()
        assert fizzbuzz.calc(1) == "1"
