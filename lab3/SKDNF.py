class SKDNF:
    def __init__(self, formula_sdnf):
        print(formula_sdnf)
        self._formula_sdnf = formula_sdnf
        self.split_sdnf = []
        self.split_formula()
        self.is_dnf = False

    def split_formula(self):
        if "|" in self._formula_sdnf:
            terms = self._formula_sdnf.split('|')
            print("sdnf formula")
            self.is_dnf = True
        else:
            terms = self._formula_sdnf.split('&')
            print("sknf formula")

        for term in terms:
            sets = list(term.strip('()'))
            variables = []
            i = 0
            while i < len(sets):
                if sets[i] == '!':
                    variables.append('!' + sets[i + 1])
                    i += 2
                else:
                    variables.append(sets[i])
                    i += 1
            self.split_sdnf.append(variables)

        print(self.split_sdnf)
        return self.split_sdnf

    @staticmethod
    def has_same_letter(pair):
        x, y = pair
        letter_x = ''.join(c for c in x if c.isalpha())
        letter_y = ''.join(c for c in y if c.isalpha())
        return letter_x == letter_y

    def find_similar_combinations(self, starter_set, non_combinable_set):
        result = []
        combined_set = []

        for i in range(len(starter_set)+1):
            buf = 0
            for j in range(i + 1, len(starter_set)):
                diff_elements = [(x, y) for x, y in zip(starter_set[i], starter_set[j]) if x != y]
                if len(diff_elements) == 1 and self.has_same_letter(diff_elements[0]):
                    new_combination = [x for x, y in zip(starter_set[i], starter_set[j]) if x == y]
                    result.append(new_combination)
                    combined_set.append(j)
                    combined_set.append(i)
                else:
                    buf += 1
                    if (buf == len(starter_set)-i-1 and (i not in combined_set) and starter_set[i] not in
                            non_combinable_set):
                        non_combinable_set.append(starter_set[i])

        if len(starter_set)-1 not in combined_set:
            non_combinable_set.append(starter_set[len(starter_set)-1])

        return result, non_combinable_set

    @staticmethod
    def remove_duplicates(lst):
        unique_elements = set(tuple(item) for item in lst)
        result = [list(item) for item in unique_elements]
        return result

    # принимает все элементы определенной строки за 1, а в остальные подставляет значения из этой строки
    @staticmethod
    def check_count(replacement, checklist):
        values_dict = {}

        for item in replacement:
            if item.startswith('!'):
                values_dict[item[1:]] = "0"
                values_dict[item] = "1"
            else:
                values_dict[item] = "1"
                values_dict['!' + item] = "0"

        new_checklist = [row[:] for row in checklist]
        for i in range(len(new_checklist)):
            for j in range(len(new_checklist[i])):
                if new_checklist[i][j] in values_dict:
                    new_checklist[i][j] = values_dict[new_checklist[i][j]]
                else:
                    new_checklist[i][j] = new_checklist[i][j]
        return new_checklist

    # проверяет, является ли конкретный элемент лишним
    @staticmethod
    def check_all_ones(checklist):
        for row in checklist:
            if all(x == '1' for x in row):
                return True
        return False

    # функция для удаления лишних элементов
    def check_extra_elements_calculation_method(self, elements):
        elements_copy = elements.copy()
        i = 0

        while i < len(elements_copy):
            current_element = elements_copy[i]
            other_elements = elements_copy[:i] + elements_copy[i + 1:]
            result = self.check_count(current_element, other_elements)
            if self.check_all_ones(result):
                del elements_copy[i]
                print(f"Удален лишний элемент: {current_element}")
            else:
                i += 1

        return elements_copy

    def minimize_calculation_method(self):
        start_set = self.split_sdnf
        non_combinable_set = []

        for i in range(0, len(self.split_sdnf[0])-1):
            if len(start_set) == 0:
                break
            start_set, non_combinable_set = self.find_similar_combinations(start_set, non_combinable_set)
            start_set = self.remove_duplicates(start_set)
            non_combinable_set = self.remove_duplicates(non_combinable_set)
            print(start_set, non_combinable_set)
        glued_formulas = non_combinable_set + start_set
        result = self.check_extra_elements_calculation_method(glued_formulas)
        print("result", result)

    def build_occurrence_table(self, implicants):
        table = [[0 for _ in range(len(self.split_sdnf))] for _ in range(len(implicants))]

        for i, row in enumerate(implicants):
            for j, col in enumerate(self.split_sdnf):
                if all(elem in col or ('!' + elem[1:]) in col for elem in row):
                    table[i][j] = 1
        print(table)

        return table

    @staticmethod
    def find_min_cover(matrix):
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        uncovered_columns = set(range(num_cols))
        selected_rows = []

        while uncovered_columns:
            best_row = -1
            best_coverage = 0
            for row in range(num_rows):
                coverage = len(uncovered_columns & set(i for i, val in enumerate(matrix[row]) if val == 1))
                if coverage > best_coverage:
                    best_coverage = coverage
                    best_row = row
            if best_row == -1:
                raise ValueError("Невозможно покрыть все столбцы с помощью данных строк")
            selected_rows.append(best_row)
            uncovered_columns -= set(i for i, val in enumerate(matrix[best_row]) if val == 1)
        return selected_rows

    def minimize_settlement_tabular_method(self):
        start_set = self.split_sdnf
        non_combinable_set = []
        for i in range(0, len(self.split_sdnf[0]) - 1):
            if len(start_set) == 0:
                break
            start_set, non_combinable_set = self.find_similar_combinations(start_set, non_combinable_set)
            start_set = self.remove_duplicates(start_set)
            non_combinable_set = self.remove_duplicates(non_combinable_set)
            print(start_set, non_combinable_set)
        glued_formulas = non_combinable_set+start_set
        table = self.build_occurrence_table(glued_formulas)
        indices = self.find_min_cover(table)
        result = [glued_formulas[i] for i in indices]

        print("result", result)

    @staticmethod
    def print_karnaugh_map(table, row, col):
        print(col)
        for i in range(len(row)):
            print(row[i], table[i])

    def build_karno_table(self, implicants):
        table = [[0 for _ in range(len(self.split_sdnf))] for _ in range(len(implicants))]

        for i, row in enumerate(implicants):
            for j, col in enumerate(self.split_sdnf):
                if all(elem in col or ('!' + elem[1:]) in col for elem in row):
                    table[i][j] = 1

        return table

    # создание комбинаций элементов для столбцов и строк в методе карно
    @staticmethod
    def get_combinations(lst, start_index, end_index):
        combinations = [[]]
        for item in lst[start_index:end_index]:
            if item.startswith('!'):
                combinations = [combo + [item[1:]] for combo in combinations] + [combo + ['!' + item[1:]] for combo in
                                                                                 combinations]
            else:
                combinations = [combo + [item] for combo in combinations] + [combo + ['!' + item] for combo in
                                                                             combinations]
        return combinations

    def generate_karnaugh_map_dnf(self):
        row = self.get_combinations(self.split_sdnf[1], 0, int(len(self.split_sdnf[1])/2))
        print(int(len(self.split_sdnf[1])/2))

        col = self.get_combinations(self.split_sdnf[1], int(len(self.split_sdnf[1])/2,), len(self.split_sdnf[1]))
        karnaugh_map = [[0 for _ in range(len(col))] for _ in range(len(row))]
        for i, implicant in enumerate(self.split_sdnf):
            for j, element_row in enumerate(row):
                if all(elem in implicant or ('!' + elem[1:]) in implicant for elem in element_row):
                    for k, element_col in enumerate(col):
                        if all(elem in implicant or ('!' + elem[1:]) in implicant for elem in element_col):
                            karnaugh_map[j][k] = 1
        return col, row, karnaugh_map

    def generate_karnaugh_map_knf(self):
        row = self.get_combinations(self.split_sdnf[1], 0, int(len(self.split_sdnf[1]) / 2))
        print(int(len(self.split_sdnf[1]) / 2))

        col = self.get_combinations(self.split_sdnf[1], int(len(self.split_sdnf[1]) / 2, ), len(self.split_sdnf[1]))
        karnaugh_map = [[1 for _ in range(len(col))] for _ in range(len(row))]
        for i, implicant in enumerate(self.split_sdnf):
            for j, element_row in enumerate(row):
                if all(elem in implicant or ('!' + elem[1:]) in implicant for elem in element_row):
                    for k, element_col in enumerate(col):
                        if all(elem in implicant or ('!' + elem[1:]) in implicant for elem in element_col):
                            karnaugh_map[j][k] = 0
        return col, row, karnaugh_map

    @staticmethod
    def find_area(matrix):
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        not_set_columns = set(range(num_cols))
        selected_rows = []

        while not_set_columns:
            best_row = -1
            best_set = 0
            for row in range(num_rows):
                current_set = len(not_set_columns & set(i for i, val in enumerate(matrix[row]) if val == 1))
                if current_set > best_set:
                    best_coverage = current_set
                    best_row = row
            selected_rows.append(best_row)
            not_set_columns -= set(i for i, val in enumerate(matrix[best_row]) if val == 1)
        return selected_rows

    def minimize_settlement_karno(self):
        start_set = self.split_sdnf
        non_combinable_set = []
        for i in range(0, len(self.split_sdnf[0]) - 1):
            if len(start_set) == 0:
                break
            start_set, non_combinable_set = self.find_similar_combinations(start_set, non_combinable_set)
            start_set = self.remove_duplicates(start_set)
            non_combinable_set = self.remove_duplicates(non_combinable_set)
        formulas = non_combinable_set + start_set
        table = self.build_karno_table(formulas)
        indices = self.find_area(table)
        result = [formulas[i] for i in indices]
        print(result)

    def minimize(self):
        if self.is_dnf:
            col, row, karnaugh_map = self.generate_karnaugh_map_dnf()
        else:
            col, row, karnaugh_map = self.generate_karnaugh_map_knf()
        self.print_karnaugh_map(karnaugh_map, row, col)
        self.minimize_settlement_karno()





t = SKDNF("(!a!bc)&(!abc)&(a!b!c)&(a!bc)&(ab!c)&(abc)")
print("Расчетный метод")
t.minimize_calculation_method()
print("Расчетно-табличный метод")
t.minimize_settlement_tabular_method()
print("Табличный метод")
print(t.minimize())
