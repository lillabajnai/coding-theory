import unittest

from tests.test_zp import TestZp
from tests.test_linear_code import TestLinearCode
from tests.test_min_distance import TestMinimumDistance

def main():
    print("\nRunning unit tests...\n")
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestZp))
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestLinearCode))
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMinimumDistance))

if __name__ == "__main__":
    main()
