import unittest
from string_calculator import add

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)
def test_single_number(self):
        self.assertEqual(add("1"), 1)
        def test_two_numbers(self):
        self.assertEqual(add("1,5"), 6)
if __name__ == '__main__':
    unittest.main()