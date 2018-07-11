import pytest

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'fizzbuzz'
    if number % 3 == 0:
        return 'fizz'
    if number % 5 == 0:
        return 'buzz'
    return number

class TestClass(object):
    def test_return_normal_number(self):
        number = 1
        assert fizzbuzz(number) == number

    def test_return_fizz_when_a_multiple_of_three(self):
        assert fizzbuzz(3) == 'fizz'

    def test_return_buzz_when_a_multiple_of_five(self):
        assert fizzbuzz(5) == 'buzz'

    def test_return_fizzbuzz_when_a_multiple_of_three_and_five(self):
        assert fizzbuzz(15) == 'fizzbuzz'
