import random


class DiagonalMatrix:
    def __init__(self, matrix):
        if len(matrix) == 16 and len(matrix[0]) == 16:
            self._matrix = matrix
        else:
            print("The matrix does not meet the conditions")

    @property
    def matrix(self):
        return self._matrix

    def print_matrix(self):
        for row in self._matrix:
            print(" ".join("1" if cell else "0" for cell in row))

    def get_word(self, i):
        word = []
        for j in range(i, len(self._matrix)):
            word.append(self._matrix[j][i])
        for j in range(0, i):
            word.append(matrix[j][i])
        return word

    def write_word(self, index_column, word):
        for i in range(index_column, len(matrix)):
            self._matrix[i][index_column] = word.pop(0)

        for i in range(index_column):
            self._matrix[i][index_column] = word.pop(0)

    def get_diagonal_column(self, index_column):
        i = index_column
        result = []
        for j in range(0, 16):
            if i == 16:
                i = 0
            result.append(self._matrix[i][j])
            i = i + 1
        return result

    def write_diagonal_column(self, column, index_column):
        i = index_column
        for j in range(0, 16):
            if i == 16:
                i = 0
            self._matrix[i][j] = column[j]
            i = i + 1

    def function_f2(self, index1, index2, index_result):
        word1 = self.get_diagonal_column(index1)
        print(word1)
        word2 = self.get_diagonal_column(index2)
        print(word2)
        result = []
        for i in range(0, len(word1)):
            if word1[i] == True and word2[i] == False:
                result.append(True)
            else:
                result.append(False)
        print("result", result)
        self.write_diagonal_column(result, index_result)
        return result

    def function_f7(self, index1, index2, index_result):
        word1 = self.get_diagonal_column(index1)
        print(word1)
        word2 = self.get_diagonal_column(index2)
        print(word2)
        result = []
        for i in range(0, len(word1)):
            if word1[i] == word2[i] == False:
                result.append(False)
            else:
                result.append(True)
        print("result", result)
        self.write_diagonal_column(result, index_result)
        return result

    def function_f8(self, index1, index2, index_result):
        word1 = self.get_diagonal_column(index1)
        print(word1)
        word2 = self.get_diagonal_column(index2)
        print(word2)
        result = []
        for i in range(0, len(word1)):
            if word1[i] == word2[i] == False:
                result.append(True)
            else:
                result.append(False)
        print("result", result)
        self.write_diagonal_column(result, index_result)
        return result

    def function_f13(self, index1, index2, index_result):
        word1 = self.get_diagonal_column(index1)
        print(word1)
        word2 = self.get_diagonal_column(index2)
        print(word2)
        result = []
        for i in range(0, len(word1)):
            if word1[i] == True and word2[i] == False:
                result.append(False)
            else:
                result.append(True)
        print("result", result)
        self.write_diagonal_column(result, index_result)
        return result

    @staticmethod
    def check_bool_list(bool_list, int_list):
        if len(bool_list) != 16 or len(int_list) != 3:
            return False
        for i in range(3):
            if bool_list[i] != (int_list[i] == 1):
                return False
        return True

    def addition(self, word):
        first_part = word[0:3]
        second_part = [False] + word[3:7]
        second_part.reverse()
        third_part = [False] + word[7:11]
        third_part.reverse()
        buf = 0
        fourth_part = []
        for i in range(0, 5):
            if int(third_part[i]) + int(second_part[i]) + buf == 3:
                fourth_part.append(True)
                buf = 1
            elif int(third_part[i]) + int(second_part[i]) + buf == 2:
                fourth_part.append(False)
                buf = 1
            elif int(third_part[i]) + int(second_part[i]) + buf == 1:
                fourth_part.append(True)
                buf = 0
            elif int(third_part[i]) + int(second_part[i]) + buf == 0:
                fourth_part.append(False)
                buf = 0
        fourth_part.reverse()
        second_part.reverse()
        third_part.reverse()
        result = first_part + second_part[1:] + third_part[1:] + fourth_part
        print(result)
        return result

    def function_addition_of_fields(self, key: list):
        buf = 0
        for i in range(len(matrix)):
            word = self.get_word(i)
            if self.check_bool_list(word, key):
                print("index for addition: ", i)
                result_word = self.addition(word)
                self.write_word(i, result_word)
            else:
                buf = buf+1

        if buf == 16:
            print("no words for addition")

    @staticmethod
    def convert_bool_list_to_number(bool_list):
        result_number = "".join("1" if x else "0" for x in bool_list)
        return int(result_number)

    @staticmethod
    def convert_to_number(number_list):
        result_number = 0
        for number in number_list:
            result_number = result_number * 10 + number
        return result_number

    def interval_search(self, smaller_bound: list, greater_bound: list):
        smaller_bound = self.convert_to_number(smaller_bound)
        greater_bound = self.convert_to_number(greater_bound)
        res_flags = [1]*16
        for i in range(len(self._matrix)):
            word = self.get_word(i)
            word = self.convert_bool_list_to_number(word)
            if word > greater_bound:
                res_flags[i] = 0

        for i in range(len(self._matrix)):
            word = self.get_word(i)
            word = self.convert_bool_list_to_number(word)
            if word < smaller_bound:
                res_flags[i] = 0

        print(res_flags)
        return res_flags







matrix = [[random.choice([True, False]) for _ in range(16)] for _ in range(16)]
print(matrix)
mat1 = DiagonalMatrix(matrix)
mat1.print_matrix()
print("f2")
mat1.function_f2(0, 1, 2)
mat1.print_matrix()
print("f7")
mat1.function_f7(0, 1, 2)
mat1.print_matrix()
print("f8")
mat1.function_f8(0, 1, 2)
mat1.print_matrix()
print("f13")
mat1.function_f13(0, 1, 2)
mat1.print_matrix()
print("addition")
mat1.function_addition_of_fields([1, 1, 1])
mat1.print_matrix()
print("search")
smaller_bound = [0]*16
greater_bound = [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mat1.interval_search(smaller_bound, greater_bound)
