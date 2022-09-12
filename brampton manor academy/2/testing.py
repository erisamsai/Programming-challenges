import unittest

from richter_2 import *


class MyFirstTests(unittest.TestCase):

    def test_richter_to_energy(self):
        self.assertEqual(richter_to_energy(1), 1995262.3149688789)


if __name__ == '__main__':
    unittest.main()
