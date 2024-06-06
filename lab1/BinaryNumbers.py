class BinaryNumber:
    def __init__(self, number):
        self._number = number
        self._binary = []
        self.point_from_end = 0
        self.convert_to_binary()

    def convert_to_binary(self):
        number = self._number
        if number == 0:
            self._binary = [0] * 16
        else:
            if number < 0:
                self._binary.append(1)
                number = - number
            else:
                self._binary.append(0)

            fractional_part_binary = self.convert_fractional_part(number)
            counter, integer_part_binary = self.convert_integer_part(number)
            self._binary += [0] * (14 - counter)
            self._binary.extend(integer_part_binary)
            self._binary.extend(fractional_part_binary)

    def convert_fractional_part(self, number):
        fractional_part_decimal = number % 1
        fractional_part_binary = []
        counter = 0
        while counter < 5:
            if fractional_part_decimal == 0.0:
                break
            counter += 1
            fractional_part_binary.append(int(fractional_part_decimal * 2))
            fractional_part_decimal = (fractional_part_decimal * 2) % 1
        self.point_from_end = counter
        return fractional_part_binary

    def convert_integer_part(self, number):
        counter = self.point_from_end
        integer_part_decimal = int(number)
        integer_part_binary = []
        while integer_part_decimal != 1:
            if counter == 15:
                print("The number has changed because it cannot be recorded")
                break
            integer_part_binary.append(integer_part_decimal % 2)
            integer_part_decimal = int(integer_part_decimal / 2)
            counter += 1
        integer_part_binary.append(1)
        integer_part_binary.reverse()
        return counter, integer_part_binary

    def print_binary_number(self):
        print(self._number)
        print(self._binary[0:16 - self.point_from_end:1], ".", self._binary[16 - self.point_from_end:16:1])

    def get_binary_code(self):
        return self._binary

    def convert_reverse_code(self):
        if self._binary[0] == 0:
            return self._binary
        reverse_code = [1]
        for element in self._binary[1:]:
            if element == 0:
                reverse_code.append(1)
            else:
                reverse_code.append(0)
        return reverse_code

    def print_reverse_code(self):
        reverse_code = self.convert_reverse_code()
        print(reverse_code[0:16 - self.point_from_end:1], ".", reverse_code[16 - self.point_from_end:16:1])

    def convert_additional_code(self):
        reverse_code = self.convert_reverse_code()
        if reverse_code[0] == 0:
            return reverse_code
        additional_code = []
        buf = 1
        for element in reverse_code[-1:0:-1]:
            if element + buf == 0:
                buf = 0
                additional_code.append(0)
            elif element + buf == 1:
                buf = 0
                additional_code.append(1)
            elif element + buf == 2:
                buf = 1
                additional_code.append(0)
        if buf == 1:
            print("The number has changed because it cannot be recorded")
        additional_code.append(1)
        additional_code.reverse()
        return additional_code

    def print_additional_code(self):
        additional_code = self.convert_additional_code()
        print(additional_code[0:16 - self.point_from_end:1], ".", additional_code[16 - self.point_from_end:16:1])

    def sum_additional_code(self, number):
        term_1 = self.convert_additional_code()
        number_2 = number
        term_2 = number_2.convert_additional_code()
        point = 0
        if self.point_from_end > number_2.point_from_end:
            term_2[1:1 + self.point_from_end - number_2.point_from_end] = []
            term_2.extend([0] * (self.point_from_end - number_2.point_from_end))
            point = self.point_from_end
        elif self.point_from_end < number_2.point_from_end:
            term_1[1:1 + number_2.point_from_end - self.point_from_end] = []
            term_1.extend([0] * (number_2.point_from_end - self.point_from_end))
            point = number_2.point_from_end
        elif self.point_from_end == number_2.point_from_end:
            point = number_2.point_from_end
        sum_code = self.sum_binary_code(term_1, term_2)
        if sum_code[0] == 1:
            sum_code = self.subtract_one(sum_code)
            for element in range(1, 16):
                if sum_code[element] == 0:
                    sum_code[element] = 1
                else:
                    sum_code[element] = 0
        return sum_code, point

    def print_sum_code(self, number):
        sum_code, point = self.sum_additional_code(number)
        print(sum_code[0:16 - point:1], ".", sum_code[16 - point:16:1])
        print(self.convert_binary_to_decimal(sum_code, point))

    @staticmethod
    def sum_binary_code(term_1, term_2):
        sum_additional_code = []
        buf = 0
        for element in range(15, -1, -1):
            if term_1[element] + term_2[element] + buf == 0:
                buf = 0
                sum_additional_code.append(0)
            elif term_1[element] + term_2[element] + buf == 1:
                buf = 0
                sum_additional_code.append(1)
            elif term_1[element] + term_2[element] + buf == 2:
                buf = 1
                sum_additional_code.append(0)
            elif term_1[element] + term_2[element] + buf == 3:
                buf = 1
                sum_additional_code.append(1)
        sum_additional_code.reverse()
        return sum_additional_code

    @staticmethod
    def subtract_one(binary_number):
        for element in range(15, -1, -1):
            if binary_number[element] == 1:
                binary_number[element] = 0
                break
            else:
                binary_number[element] = 1
        return binary_number

    @staticmethod
    def convert_binary_to_decimal(binary_code, point):
        power = -1 * point
        number = 0
        for i in range(15, 0, -1):
            number += (binary_code[i] * (2 ** power))
            power += 1
        if binary_code[0] == 1:
            number *= -1
        return number

    def multiply_numbers(self, number):
        number_zero = 0
        multiplication_code = [0] * 16
        number_2 = number.get_binary_code()
        print(number_2)
        print(self._binary)
        for i in range(15, 0, -1):
            buf = [0] * number_zero
            for j in range(15, -1, -1):
                if len(buf) < 16:
                    buf.append(self._binary[i] * number_2[j])
            buf.reverse()
            multiplication_code = self.sum_binary_code(multiplication_code, buf)
            buf.clear()
            number_zero += 1
        if number_2[0] == self._binary[0]:
            multiplication_code[0] = 0
        else:
            multiplication_code[0] = 1
        point = number.point_from_end + self.point_from_end
        return multiplication_code, point

    def print_multiplication(self, number_2):
        multiplication_code, point = self.multiply_numbers(number_2)
        print(multiplication_code[0:16 - point:1], ".", multiplication_code[16 - point:16:1])
        print(self.convert_binary_to_decimal(multiplication_code, point))

    @staticmethod
    def difference(reduced, subtracted):
        diff = len(reduced) - len(subtracted)
        if diff > 0:
            subtracted = [0] * diff + subtracted
        elif diff < 0:
            reduced = [0] * abs(diff) + reduced
        result = []
        borrow = 0
        for i in range(len(reduced) - 1, -1, -1):
            digit1 = reduced[i]
            digit2 = subtracted[i]
            diff = digit1 - digit2 - borrow
            if diff < 0:
                diff += 2
                borrow = 1
            else:
                borrow = 0
            result.insert(0, diff)
        while len(result) > 1 and result[0] == 0:
            result.pop(0)
        return result

    def divide_process(self, dividend, divisor):
        present_dividend = dividend[:len(divisor)]
        divide_result = []
        if len(present_dividend) < len(divisor):
            point = 5 - (len(divisor) - len(present_dividend))
        else:
            point = 0
        for i in range(len(divisor), len(dividend) + 6, 1):
            if int(''.join(map(str, divisor))) <= int(''.join(map(str, present_dividend))):
                first_one_index = next((i for i, x in enumerate(present_dividend) if x == 1), None)
                if first_one_index is not None:
                    present_dividend = present_dividend[first_one_index:]
                divide_result.append(1)
                present_dividend = self.difference(present_dividend, divisor)
                if i < len(dividend):
                    present_dividend.append(dividend[i])
                else:
                    present_dividend = present_dividend[0:] + [0]
            else:
                if i < len(dividend):
                    present_dividend.append(dividend[i])
                    divide_result.append(0)
                else:
                    present_dividend = present_dividend[0:] + [0]
                    divide_result.append(0)
        if len(divide_result) < 5 & all(item == 0 for item in divide_result) or divide_result == [0]:
            divide_result = [0] * 5
        return divide_result, point

    @staticmethod
    def edit_divide(div_res, sign, point_from_process):
        if len(div_res) > 5:
            point = len(div_res[0:]) - 5
        else:
            point = len(div_res[0:]) - point_from_process
        for i in range(len(div_res[0:])-1, len(div_res[0:])-6, -1):
            if div_res[i] == 0:
                del div_res[i]
            else:
                break
        point = len(div_res) - point
        div_res = [sign] + [0]*(16 - len(div_res)-1) + div_res
        return div_res, point

    def divide_numbers(self, number):
        dividend = []  # делимое
        divisor = []  # делитель
        for element in range(1, 16, 1):
            if self._binary[element] == 1:
                dividend = self._binary[element:]
                break
        for element in range(1, 16, 1):
            if number.get_binary_code()[element] == 1:
                divisor = number.get_binary_code()[element:]
                break
        result, point_process = self.divide_process(dividend, divisor)
        if number.get_binary_code()[0] == 0 & self._binary[0] == 0:
            sign = 0
        else:
            sign = 1
        result, point = self.edit_divide(result, sign, point_process)
        print(result[0:16 - point:1], ".", result[16 - point:16:1])
        print(self.convert_binary_to_decimal(result, point))
        return result, point


print("number")
number2 = BinaryNumber(3)
number2.print_binary_number()
number2.print_reverse_code()
number2.print_additional_code()
number12 = BinaryNumber(5)
number12.print_binary_number()
print("sum")
number12.print_sum_code(number2)
print("multiplication")
number12.print_multiplication(number2)
print("divide")
number100 = BinaryNumber(15)
number100.print_binary_number()
number4 = BinaryNumber(4)
number4.print_binary_number()
number100.divide_numbers(number4)
