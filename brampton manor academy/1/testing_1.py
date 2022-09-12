import unittest

from rod_conversions_1 import *

class MyFirstTests(unittest.TestCase):

    def test_rods_to_meters(self):
        self.assertEqual(rods_to_meters(1), 5.0292)

    def test_meters_to_miles(self):
        self.assertEqual(meters_to_miles(5.0292), 0.0031250077671592085)

if __name__ == '__main__':
    unittest.main()
