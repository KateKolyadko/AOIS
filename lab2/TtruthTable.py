import re
import itertools


class TruthTable:
    def __init__(self, formula):
        self._formula = formula
        self._table = []
        self.operations = []
        print(self._formula)
        self.create_operations()
        self.create_combinations()
        self.count()

    @property
    def table(self):
        return self._table

    @staticmethod
    def logical_and(value_1, value_2):
        if value_2 == 1 & value_1 == 1:
            return 1
        else:
            return 0

    @staticmethod
    def logical_or(value_1, value_2):
        if value_2 == 0 and value_1 == 0:
            return 0
        else:
            return 1

    @staticmethod
    def equivalence(value_1, value_2):
        if value_2 == value_1:
            return 1
        else:
            return 0

    @staticmethod
    def implication(value_1, value_2):
        if value_2 == 0 and value_1 == 1:
            return 0
        else:
            return 1

    @staticmethod
    def logical_not(value_1):
        if value_1 == 0:
            return 1
        else:
            return 0

    def create_combinations(self):
        variables = re.findall(r'[a-zA-Z]', self._formula)
        combinations = list(itertools.product([str(0), str(1)], repeat=len(set(variables))))
        for combo in combinations:
            self._table.append(list(combo))

    def create_operations(self):
        letters = re.findall(r'[a-zA-Z]', self._formula)
        self.operations = list(set(letters))
        self.operations.sort()
        begin = 0
        for i, element in enumerate(self._formula):
            if element == "(" or element == "!":
                begin = i
            elif element == ")" or (self._formula[begin] == "!" and element.isalpha()):
                self.operations.append(self._formula[begin:i + 1])
                for j in range(begin - 1, -1, -1):
                    if self._formula[j] == "!" or self._formula[j] == "(":
                        begin = j
                        break
            elif self._formula[begin] == "!" and self._formula[begin + 1] == "(" and self._formula[i - 1] == ")":
                self.operations.append(self._formula[begin:i])
                for j in range(begin - 1, -1, -1):
                    if self._formula[j] == "(" or self._formula[j] == "!":
                        begin = j
                        break

    def determine_value(self, counting_expression):
        if counting_expression.startswith("!"):
            value1 = int(counting_expression[1])
            return self.logical_not(value1)
        elif counting_expression.startswith("(") and counting_expression.endswith(")"):
            counting_expression = counting_expression[1:-1].strip()
            value1 = int(counting_expression[0])
            if len(counting_expression) == 3 and (counting_expression[1] == "&" or counting_expression[1] == "|" or
                                                  counting_expression[1] == "~"):
                value2 = int(counting_expression[2])
                if counting_expression[1] == "&":
                    return self.logical_and(value1, value2)
                elif counting_expression[1] == "|":
                    return self.logical_or(value1, value2)
                elif counting_expression[1] == "~":
                    return self.equivalence(value1, value2)
            elif len(counting_expression) == 4 and counting_expression[1:3] == "->":
                value2 = int(counting_expression[3])
                return self.implication(value1, value2)
            else:
                raise ValueError("Неверный формат входной строки:")

    def count(self):
        variables = re.findall(r'[a-zA-Z]', self._formula)
        start_index = len(set(variables))
        for i, operation in enumerate(self.operations[start_index:], start=start_index):
            for j in range(1, len(self._table) + 1):
                counting_expression = operation
                for k in range(i - 1, -1, -1):
                    if self.operations[k] in counting_expression:
                        counting_expression = counting_expression.replace(self.operations[k], self._table[j - 1][k])
                counting_expression = str(self.determine_value(counting_expression))
                self._table[j - 1].append(counting_expression)

        print(self.operations)
        for row in self._table:
            print(row)

    def create_sknf(self):
        variables = re.findall(r'[a-zA-Z]', self._formula)
        start_index = len(set(variables))
        sknf = ""
        numeric_sknf = ""
        for i in range(0, len(self._table)):
            if int(self._table[i][len(self.operations)-1]) == 0:
                combination = ""
                numeric_sknf = numeric_sknf + str(i) + ", "
                for j in range(0, start_index):
                    if int(self._table[i][j]) == 0:
                        combination = combination + self.operations[j]
                        if j != start_index-1:
                            combination = combination + "|"
                    else:
                        combination = combination + "!" + self.operations[j]
                        if j != start_index - 1:
                            combination = combination + "|"
                sknf = sknf + "(" + combination + ")" + "&"
        sknf = sknf[:-1]
        numeric_sknf = "(" + numeric_sknf[:-2] + ") &"
        print(sknf)
        print(numeric_sknf)
        return sknf, numeric_sknf

    def create_sdnf(self):
        variables = re.findall(r'[a-zA-Z]', self._formula)
        start_index = len(set(variables))
        sdnf = ""
        numeric_sdnf = ""
        for i in range(0, len(self._table)):
            if int(self._table[i][len(self.operations) - 1]) == 1:
                combination = ""
                numeric_sdnf = numeric_sdnf + str(i) + ", "
                for j in range(0, start_index):
                    if int(self._table[i][j]) == 1:
                        combination = combination + self.operations[j]
                        if j != start_index - 1:
                            combination = combination + "&"
                    else:
                        combination = combination + "!" + self.operations[j]
                        if j != start_index - 1:
                            combination = combination + "&"
                sdnf = sdnf + "(" + combination + ")" + "|"
        sdnf = sdnf[:-1]
        numeric_sdnf = "(" + numeric_sdnf[:-2] + ") |"
        print(sdnf)
        print(numeric_sdnf)
        return sdnf, numeric_sdnf


    def convert_binary_to_decimal(binary_code, point):
        power = -1
        number = 0
        for i in range(15, 0, -1):
            number += (binary_code[i] * (2 ** power))
            power += 1
        if binary_code[0] == 1:
            number *= -1
        return number

    def create_index_form(self):
        index = [row[len(self.operations)-1] for row in self._table]
        power = 0
        number = 0
        for i in range(len(index)-1, -1, -1):
            number += (int(index[i]) * (2 ** power))
            power += 1
        print(number, "-", index)
        return number, index


t = TruthTable("(a|(b&!c))")
print("SKNF")
t.create_sknf()
print("SDNF")
t.create_sdnf()
print("index form")
t.create_index_form()


