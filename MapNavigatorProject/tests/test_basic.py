import unittest
# Using for the testing purpose only. Implementing with the basic test cases.
class TestBasic(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()
