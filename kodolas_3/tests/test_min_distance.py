import unittest
import numpy as np

from src.min_distance import min_distance


class TestMinimumDistance(unittest.TestCase):

    def test_Z2(self):
        codewords = [np.array([1, 1, 0]), np.array([0, 1, 1])]
        expected = 2
        result = min_distance(codewords)
        print(f"Test Z2: Codewords: {codewords}, Result: {result}, Expected: {expected}")
        self.assertEqual(result, expected)

    def test_Z3(self):
        codewords = [np.array([1, 2, 0]), np.array([2, 1, 1]), np.array([0, 1, 1])]
        expected = 1
        result = min_distance(codewords)
        print(f"Test Z3: Codewords: {codewords}, Result: {result}, Expected: {expected}")
        self.assertEqual(result, expected)

    def test_Z5(self):
        codewords = [np.array([1, 2, 0]), np.array([2, 1, 3]), np.array([4, 0, 1])]
        expected = 3
        result = min_distance(codewords)
        print(f"Test Z5: Codewords: {codewords}, Result: {result}, Expected: {expected}")
        self.assertEqual(result, expected)

    def test_single_codeword(self):
        codewords = [np.array([1])]
        expected = float('inf')
        result = min_distance(codewords)
        print(f"Test single codeword: Codewords: {codewords}, Result: {result}, Expected: {expected}")
        self.assertEqual(result, expected)

    def test_empty_list(self):
        codewords = []
        expected = float('inf')
        result = min_distance(codewords)
        print(f"Test empty list: Codewords: {codewords}, Result: {result}, Expected: {expected}")
        self.assertEqual(result, expected)

    def test_Z5_random_large(self):
        np.random.seed(42)
        codewords = [np.random.randint(0, 5, size=10) for _ in range(100)]
        expected = 1 # ez itt mindig más lesz a random miatt
        result = min_distance(codewords)
        print(f"Test Z5 Random Large: Codewords: {codewords[:3]}..., Result: {result}, Expected: {expected}")
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
