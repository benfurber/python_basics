import pytest
import airport as subject

class TestClass(object):
    def test_airport_can_be_initialised(self):
        airport_name = 'Heathrow'
        airport = subject.Airport(airport_name)

        assert airport.name == airport_name
