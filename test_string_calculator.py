import unittest
from string_calculator import add

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

if __name__ == '__main__':
    unittest.main()