import unittest

# Fungsi yang akan diuji
def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_mixed_numbers(self):
        result = add(2, -3)
        self.assertEqual(result, -1)

    def test_add_zero(self):
        result = add(0, 5)
        self.assertEqual(result, 5)

if __name__ == "__main":
    unittest.main()
