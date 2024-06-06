import unittest
from BinaryNumbers import BinaryNumber


class MyTestCase(unittest.TestCase):
    def test_convert_to_binary_zero(self):
        binary_number = BinaryNumber(0)
        binary_code = binary_number.get_binary_code()
        expected_binary_code = [0] * 16
        self.assertEqual(binary_code, expected_binary_code)

    def test_convert_to_binary_positive_integer(self):
        binary_number = BinaryNumber(10)
        binary_code = binary_number.get_binary_code()
        expected_binary_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
        self.assertEqual(binary_code, expected_binary_code)

    def test_convert_to_binary_negative_integer(self):
        binary_number = BinaryNumber(-10)
        binary_code = binary_number.get_binary_code()
        expected_binary_code = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
        self.assertEqual(binary_code, expected_binary_code)

    def test_convert_reverse_code_positive_integer(self):
        binary_number = BinaryNumber(10)
        reverse_code = binary_number.convert_reverse_code()
        expected_reverse_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
        self.assertEqual(reverse_code, expected_reverse_code)

    def test_convert_reverse_code_negative_integer(self):
        binary_number = BinaryNumber(-10)
        reverse_code = binary_number.convert_reverse_code()
        expected_reverse_code = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1]
        self.assertEqual(reverse_code, expected_reverse_code)

    def test_convert_additional_code_positive_integer(self):
        binary_number = BinaryNumber(10)
        additional_code = binary_number.convert_additional_code()
        expected_additional_code = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
        self.assertEqual(additional_code, expected_additional_code)

    def test_convert_additional_code_negative_integer(self):
        binary_number = BinaryNumber(-10)
        additional_code = binary_number.convert_additional_code()
        expected_additional_code = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.assertEqual(additional_code, expected_additional_code)


if __name__ == '__main__':
    unittest.main()
