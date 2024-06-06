import unittest
from BinaryFloat import BinaryFloat


class MyTestCase(unittest.TestCase):
    def test_convert_to_binary_float_zero(self):
        binary_float = BinaryFloat(0)
        binary_code = binary_float.binary_float
        expected_binary_code = [0] * 32
        self.assertEqual(binary_code, expected_binary_code)

    def test_convert_to_binary_float_positive_integer(self):
        binary_float = BinaryFloat(10)
        binary_code = binary_float.binary_float
        expected_binary = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0]
        self.assertEqual(binary_code, expected_binary)

    def test_convert_to_binary_float_negative_integer(self):
        binary_float = BinaryFloat(-10)
        binary_code = binary_float.binary_float
        expected_binary = [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0]
        self.assertEqual(binary_code, expected_binary)

    def test_sum_binary_float(self):
        float_1 = BinaryFloat(10)
        float_2 = BinaryFloat(10)
        expected_binary = [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0]
        self.assertEqual(float_1.sum_binary_float(float_2), expected_binary)


if __name__ == '__main__':
    unittest.main()
