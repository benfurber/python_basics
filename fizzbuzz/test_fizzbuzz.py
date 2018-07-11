import pytest
import fizzbuzz as fb

class TestClass(object):
    def test_return_normal_number(self):
        number = 1
        assert fb.fizzbuzz(number) == number

    def test_return_fizz_when_a_multiple_of_three(self):
        assert fb.fizzbuzz(3) == 'fizz'

    def test_return_buzz_when_a_multiple_of_five(self):
        assert fb.fizzbuzz(5) == 'buzz'

    def test_return_fizzbuzz_when_a_multiple_of_three_and_five(self):
        assert fb.fizzbuzz(15) == 'fizzbuzz'
