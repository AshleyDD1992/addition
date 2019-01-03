import unittest
from addition import addition

class MyAdditionFunc(unittest.TestCase):
    def test_add_a_to_b(self):
        self.assertEqual(addition(2, 2), 4)

if __name__ == "__main__":
    unittest.main()