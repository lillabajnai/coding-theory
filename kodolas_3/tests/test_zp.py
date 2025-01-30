import unittest

import numpy as np

from src.zp import Zp


class TestZp(unittest.TestCase):

    def setUp(self):
        self.zp = Zp(7)

    def test_add(self):
        inputs = [(3, 5), (6, 2), (0, 0), (7, 1), (-1, 2)]
        expected_results = [1, 1, 0, 1, 1]

        for (a, b), expected in zip(inputs, expected_results):
            result = self.zp.add(a, b)
            print(f'add({a}, {b}) = {result} (Expected: {expected})')
            self.assertEqual(result, expected)

    def test_sub(self):
        inputs = [(3, 5), (6, 2), (0, 0), (0, 1), (6, 7)]
        expected_results = [5, 4, 0, 6, 6]

        for (a, b), expected in zip(inputs, expected_results):
            result = self.zp.sub(a, b)
            print(f'sub({a}, {b}) = {result} (Expected: {expected})')
            self.assertEqual(result, expected)

    def test_mul(self):
        inputs = [(3, 5), (6, 2), (0, 0), (0, 5), (3, -1), (7, 3)]
        expected_results = [1, 5, 0, 0, 6, 2]

        for (a, b), expected in zip(inputs, expected_results):
            result = self.zp.mul(a, b)
            print(f'mul({a}, {b}) = {result} (Expected: {expected})')
            self.assertEqual(result, expected)

    def test_inv(self):
        inputs = [3, 5]
        expected_results = [5, 3]

        for a, expected in zip(inputs, expected_results):
            result = self.zp.inv(a)
            print(f'inv({a}) = {result} (Expected: {expected})')
            self.assertEqual(result, expected)

        with self.assertRaises(ValueError):
            self.zp.inv(0)

    def test_div(self):
        inputs = [(3, 5), (6, 2), (1, 3)]
        expected_results = [2, 3, 5]

        for (a, b), expected in zip(inputs, expected_results):
            result = self.zp.div(a, b)
            print(f'div({a}, {b}) = {result} (Expected: {expected})')
            self.assertEqual(result, expected)

    def test_matrix_multiplication(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        result = self.zp.mat_mul(A, B)
        expected = np.array([[19 % 7, 22 % 7], [43 % 7, 50 % 7]])
        print(f'mat_mul(A, B) = \n{result} (Expected: \n{expected})')
        np.testing.assert_array_equal(result, expected)


if __name__ == '__main__':
    unittest.main()
