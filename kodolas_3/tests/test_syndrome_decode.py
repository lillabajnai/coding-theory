import unittest

import numpy as np

from src.syndrome_decode import syndrome_decode


class TestSyndromeDecode(unittest.TestCase):

    def test_syndrome_decode(self):
        H = np.array([[1, 0, 0, 0, 0, 1, 1],
                      [0, 1, 0, 0, 1, 0, 1],
                      [0, 0, 1, 0, 1, 1, 0],
                      [0, 0, 0, 1, 1, 1, 1]])

        received = np.array([1, 1, 1, 0, 1, 0, 1])
        expected = np.array([1, 0, 1, 0, 1, 0, 1])
        expected_error_position = 2

        decoded, error_position = syndrome_decode(H, received)

        print(f"Generátor mátrix:\n{H}")
        print(f"Kódszó: {received}")
        print(f"Dekódolt üzenet: {decoded}")
        print(f"Hiba a {error_position}. biten volt." if error_position else "Nincs hiba.")
        print(f"Elvárt eredmény: {expected}")

        np.testing.assert_array_equal(decoded, expected)
        self.assertEqual(error_position, expected_error_position)

    def test_no_error(self):
        H = np.array([[1, 0, 0, 0, 0, 1, 1],
                      [0, 1, 0, 0, 1, 0, 1],
                      [0, 0, 1, 0, 1, 1, 0],
                      [0, 0, 0, 1, 1, 1, 1]])

        received = np.array([1, 0, 1, 0, 1, 0, 1])  # Hibamentes kódszó
        expected = np.array([1, 0, 1, 0, 1, 0, 1])

        decoded, error_position = syndrome_decode(H, received)

        print(f"Generátor mátrix:\n{H}")
        print(f"Kódszó: {received}")
        print(f"Dekódolt üzenet: {decoded}")
        print(f"Hiba a {error_position}. biten volt." if error_position else "Nincs hiba.")
        print(f"Elvárt eredmény: {expected}")

        np.testing.assert_array_equal(decoded, expected)
        self.assertIsNone(error_position)  # Nincs hiba


if __name__ == '__main__':
    unittest.main()