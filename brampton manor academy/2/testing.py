import unittest

from richter_2 import *


class MyFirstTests(unittest.TestCase):

    def test_richter_to_energy(self):
        self.assertEqual(richter_to_energy(1), 1995262.3149688789)
        
    def test_energy_to_tnt(self):
        self.assertEqual(energy_to_tnt(1), 0.00047687913837688307)

if __name__ == '__main__':
    unittest.main()
