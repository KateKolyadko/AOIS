class BinaryFloat:
    def __init__(self, number):
        self._number = number
        self._binary_float = []
        self.convert_to_binary_float()

    @property
    def binary_float(self):
        return self._binary_float

    @staticmethod
    def _convert_integer_part(number):
        integer_part_decimal = int(number)
        integer_part_binary = []
        if integer_part_decimal == 0:
            integer_part_binary = [0]
        else:
            while integer_part_decimal != 1:
                integer_part_binary.append(integer_part_decimal % 2)
                integer_part_decimal = int(integer_part_decimal // 2)
            integer_part_binary.append(1)
            integer_part_binary.reverse()
        return integer_part_binary

    @staticmethod
    def _convert_fractional_part(number):
        fractional_part_decimal = number % 1
        fractional_part_binary = []
        while fractional_part_decimal != 0.0:
            fractional_part_binary.append(int(fractional_part_decimal * 2))
            fractional_part_decimal = (fractional_part_decimal * 2) % 1
        return fractional_part_binary

    def _determine_the_sign(self):
        if self._number >= 0:
            sign = 0
        else:
            sign = 1
        return sign

    def convert_to_binary_float(self):
        sign = self._determine_the_sign()
        number = self._number
        if sign == 1:
            number = - self._number
        int_part = self._convert_integer_part(number)
        fractional_part = self._convert_fractional_part(number)
        mantissa = int_part + fractional_part
        if 1 in mantissa:
            mantissa = mantissa[mantissa.index(1)+1:]
        mantissa = mantissa[:23]
        if len(mantissa) < 23:
            mantissa = mantissa + [0]*(23-len(mantissa))
        if int(''.join(map(str, int_part))) >= 1:
            exp = self._convert_integer_part(127 + len(int_part) - 1)
        elif number == 0:
            exp = [0]*8
        else:
            exp = self._convert_integer_part(127 - fractional_part.index(1) - 1)
        if len(exp) <= 8:
            exp = [0] * (8-len(exp)) + exp
        else:
            exp = exp[:8]
        self._binary_float = [sign] + exp + mantissa
        self._binary_float = [sign] + exp + mantissa
        print(self._binary_float)

    def convert_binary_to_decimal(self):
        power = 0
        number = 0
        for i in range(8, 0, -1):
            number += (self._binary_float[i] * (2 ** power))
            power += 1
        return number

    @staticmethod
    def sum_one(number):
        buf = 1
        result = []
        for element in range(len(number)-1, -1, -1):
            if number[element] + buf == 1:
                result.append(1)
                buf = 0
            elif number[element] + buf == 2:
                result.append(0)
                buf = 1
            else:
                result.append(0)
                buf = 0
        if buf == 1:
            result.append(1)
        result.reverse()
        return result

    def sum_process(self, addendum_2, exp):
        addendum_1 = [1] + self._binary_float[9:32]
        summa = []
        buf = 0
        for element in range(22, -1, -1):
            if addendum_1[element] + addendum_2[element] + buf == 0:
                buf = 0
                summa.append(0)
            elif addendum_1[element] + addendum_2[element] + buf == 1:
                buf = 0
                summa.append(1)
            elif addendum_1[element] + addendum_2[element] + buf == 2:
                buf = 1
                summa.append(0)
            elif addendum_1[element] + addendum_2[element] + buf == 3:
                buf = 1
                summa.append(1)
        if buf == 1:
            summa.append(1)
        summa.reverse()
        if len(summa) > 23:
            exp = self.sum_one(exp)[0:8]
            summa = exp + summa[1:24]
        else:
            summa = exp + summa[1:24] + [0]
        return summa

    def sum_binary_float(self, number_2):
        exp1 = self.convert_binary_to_decimal()
        exp2 = number_2.convert_binary_to_decimal()
        diff = abs(exp1 - exp2)
        summa = []
        if exp1 >= exp2:
            addendum = [0] * diff + [1] + number_2.binary_float[9:31 - diff]
            summa = self.binary_float[:1] + self.sum_process(addendum, self.binary_float[1:9])
        elif exp1 < exp2:
            addendum = [0] * diff + [1] + self.binary_float[9:31 - diff]
            summa = number_2.binary_float[:1] + number_2.sum_process(addendum, number_2.binary_float[1:9])
        print(summa)
        return summa


float_1 = BinaryFloat(1.5)
float_2 = BinaryFloat(15.5)
float_1.sum_binary_float(float_2)
