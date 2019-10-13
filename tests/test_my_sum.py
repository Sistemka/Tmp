import unittest

from src.my_sum import my_sum

class TestSum(unittest.TestCase):

    def test_my_sum(self):
        self.assertEqual(my_sum(2, 3), 5, "Should be 5")
        self.assertEqual(my_sum(10, 7), 17, "Should be 17")
        self.assertEqual(my_sum(-2, -10), -12, "Should be -12")
