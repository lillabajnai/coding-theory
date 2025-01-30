import unittest
import numpy as np
from src.linear_code import LinearCode

class TestLinearCode(unittest.TestCase):

    def setUp(self):
        self.G = np.array([[1, 0, 0, 1, 1, 0, 1],
                      [0, 1, 0, 1, 0, 1, 1],
                      [0, 0, 1, 0, 1, 1, 1]])
        self.code = LinearCode(self.G, 2)

    def test_encode(self):
        message = [1, 0, 1]
        print(f"\nTest: Encoding with message: {message}")
        print(f"Generator matrix (G):\n{self.G}")
        encoded_message = self.code.encode(message)
        expected = np.array([1, 0, 1, 1, 0, 1, 0])
        print(f"Result: {encoded_message}")
        print(f"Expected: {expected}")
        np.testing.assert_array_equal(encoded_message, expected)

    def test_encode_all_zeros(self):
        message = [0, 0, 0]
        print(f"\nTest: Encoding with message: {message}")
        print(f"Generator matrix (G):\n{self.G}")
        encoded_message = self.code.encode(message)
        expected = np.array([0, 0, 0, 0, 0, 0, 0])
        print(f"Result: {encoded_message}")
        print(f"Expected: {expected}")
        np.testing.assert_array_equal(encoded_message, expected)

    def test_encode_all_ones(self):
        message = [1, 1, 1]
        print(f"\nTest: Encoding with message: {message}")
        print(f"Generator matrix (G):\n{self.G}")
        encoded_message = self.code.encode(message)
        expected = np.array([1, 1, 1, 0, 0, 0, 1])
        print(f"Result: {encoded_message}")
        print(f"Expected: {expected}")
        np.testing.assert_array_equal(encoded_message, expected)

    def test_invalid_message_length(self):
        message = [1, 1]
        with self.assertRaises(ValueError):
            self.code.encode(message)

if __name__ == '__main__':
    unittest.main()
