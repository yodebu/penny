import unittest
import csv
from penny.value_checks import *
import os

class ValueChecksTest(unittest.TestCase):
    def test_is_a_bool(self):
        pass

    def test_is_a_int(self):
        assert not is_a_int("50.15")
        assert not is_a_int(50.15)
        assert is_a_int("120938123")
        assert is_a_int(9283948324)

    def test_is_a_float(self):
        assert is_a_float("50.15")
        assert not is_a_float(100)

    def test_is_a_date(self):
        assert not is_a_date('ST')
        assert is_a_date('31-May-13')

    def is_a_coord(self):
        assert not is_a_coord(190)
        assert not is_a_coord('hello!')
        assert not is_a_coord(179.999999999999999999123123)
        assert is_a_coord("78.1")
        assert is_a_coord("-179.123")
        assert is_a_coord(170, key='lng')
        assert not is_a_coord(150)

    def is_a_coord_pair(self):
        assert is_a_coord_pair("-37.123,148")
        assert is_a_coord_pair("180,89.1234")
        assert is_a_coord_pair("-37.123|148")
        assert is_a_coord_pair("180|89.1234")
        assert is_a_coord_pair("-37.123/148")
        assert is_a_coord_pair("180/89.1234")
        assert not is_a_coord_pair("180,91")
        assert not is_a_coord_pair("-181,-90")
        assert not is_a_coord_pair("-181.23,45")
        assert not is_a_coord_pair("91,91")


def main():
    unittest.main()

if __name__ == "__main__":
    main()