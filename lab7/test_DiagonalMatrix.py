import unittest
from DiagonalMatrix import DiagonalMatrix


class TestDiagonalMatrix(unittest.TestCase):
    def test_f2(self):
        matrix = [[True, True, False, False, False, True, True, False, False, True, False, False, True, False, True,
                   True], [True, True, True, False, False, False, True, True, False, False, True, False, True, False,
                           True, False], [False, True, True, True, True, False, False, False, False, False, True, True,
                                          True, True, False, False], [True, False, True, True, True, False, False,
                                                                      False, True, False, True, False, True, True, True,
                                                                      True], [False, False, True, False, True, True,
                                                                              True, True, True, True, True, False, True,
                                                                              True, False, True], [False, True, True,
                                                                                                   True, False, True,
                                                                                                   False, False, True,
                                                                                                   False, True, True,
                                                                                                   True, True, False,
                                                                                                   False], [True, False,
                                                                                                            False, True,
                                                                                                            False,
                                                                                                            False, True,
                                                                                                            False, True,
                                                                                                            False, True,
                                                                                                            True, True,
                                                                                                            False, True,
                                                                                                            True],
                  [False, False, True, True, True, True, False, True, True, True, True, False, True, False, False,
                   True], [False, True, False, False, True, True, False, False, True, True, False, False, True, False,
                           True, True], [True, False, True, False, True, True, True, False, True, True, False, False,
                                         False, True, True, True], [False, True, False, True, True, False, False, True,
                                                                    False, False, True, True, False, False, False,
                                                                    False], [True, True, False, False, True, True,
                                                                             False, False, True, False, False, False,
                                                                             False, True, True, True], [True, False,
                                                                                                        False, True,
                                                                                                        True, False,
                                                                                                        True, False,
                                                                                                        False, False,
                                                                                                        False, False,
                                                                                                        True, True,
                                                                                                        True, False],
                  [False, False, False, True, False, False, False, False, False, True, False, False, False, False,
                   True, False], [False, False, False, False, False, True, True, False, True, False, False, True, True,
                                  True, False, False], [True, True, True, False, False, False, True, False, False,
                                                        False, True, True, True, True, False, False]]
        matr1 = DiagonalMatrix(matrix)
        self.assertEqual(matr1.function_f2(0, 1, 2), [False, False, False, True, True,
                                                      True, True, True, False, True, True, False, True, False, False,
                                                      False])

    def test_f7(self):
        matrix = [[True, True, False, False, False, True, True, False, False, True, False, False, True, False, True,
                   True], [True, True, True, False, False, False, True, True, False, False, True, False, True, False,
                           True, False], [False, True, True, True, True, False, False, False, False, False, True, True,
                                          True, True, False, False], [True, False, True, True, True, False, False,
                                                                      False, True, False, True, False, True, True, True,
                                                                      True], [False, False, True, False, True, True,
                                                                              True, True, True, True, True, False, True,
                                                                              True, False, True], [False, True, True,
                                                                                                   True, False, True,
                                                                                                   False, False, True,
                                                                                                   False, True, True,
                                                                                                   True, True, False,
                                                                                                   False], [True, False,
                                                                                                            False, True,
                                                                                                            False,
                                                                                                            False, True,
                                                                                                            False, True,
                                                                                                            False, True,
                                                                                                            True, True,
                                                                                                            False, True,
                                                                                                            True],
                  [False, False, True, True, True, True, False, True, True, True, True, False, True, False, False,
                   True], [False, True, False, False, True, True, False, False, True, True, False, False, True, False,
                           True, True], [True, False, True, False, True, True, True, False, True, True, False, False,
                                         False, True, True, True], [False, True, False, True, True, False, False, True,
                                                                    False, False, True, True, False, False, False,
                                                                    False], [True, True, False, False, True, True,
                                                                             False, False, True, False, False, False,
                                                                             False, True, True, True], [True, False,
                                                                                                        False, True,
                                                                                                        True, False,
                                                                                                        True, False,
                                                                                                        False, False,
                                                                                                        False, False,
                                                                                                        True, True,
                                                                                                        True, False],
                  [False, False, False, True, False, False, False, False, False, True, False, False, False, False,
                   True, False], [False, False, False, False, False, True, True, False, True, False, False, True, True,
                                  True, False, False], [True, True, True, False, False, False, True, False, False,
                                                        False, True, True, True, True, False, False]]
        matr1 = DiagonalMatrix(matrix)
        self.assertEqual(matr1.function_f7(0, 1, 2), [True, True, True, True, True, True,
                                                      True, True, True, True, True, False, True, True, False, True])

    def test_f8(self):
        matrix = [[True, True, False, False, False, True, True, False, False, True, False, False, True, False, True,
                   True], [True, True, True, False, False, False, True, True, False, False, True, False, True, False,
                           True, False], [False, True, True, True, True, False, False, False, False, False, True, True,
                                          True, True, False, False], [True, False, True, True, True, False, False,
                                                                      False, True, False, True, False, True, True, True,
                                                                      True], [False, False, True, False, True, True,
                                                                              True, True, True, True, True, False, True,
                                                                              True, False, True], [False, True, True,
                                                                                                   True, False, True,
                                                                                                   False, False, True,
                                                                                                   False, True, True,
                                                                                                   True, True, False,
                                                                                                   False], [True, False,
                                                                                                            False, True,
                                                                                                            False,
                                                                                                            False, True,
                                                                                                            False, True,
                                                                                                            False, True,
                                                                                                            True, True,
                                                                                                            False, True,
                                                                                                            True],
                  [False, False, True, True, True, True, False, True, True, True, True, False, True, False, False,
                   True], [False, True, False, False, True, True, False, False, True, True, False, False, True, False,
                           True, True], [True, False, True, False, True, True, True, False, True, True, False, False,
                                         False, True, True, True], [False, True, False, True, True, False, False, True,
                                                                    False, False, True, True, False, False, False,
                                                                    False], [True, True, False, False, True, True,
                                                                             False, False, True, False, False, False,
                                                                             False, True, True, True], [True, False,
                                                                                                        False, True,
                                                                                                        True, False,
                                                                                                        True, False,
                                                                                                        False, False,
                                                                                                        False, False,
                                                                                                        True, True,
                                                                                                        True, False],
                  [False, False, False, True, False, False, False, False, False, True, False, False, False, False,
                   True, False], [False, False, False, False, False, True, True, False, True, False, False, True, True,
                                  True, False, False], [True, True, True, False, False, False, True, False, False,
                                                        False, True, True, True, True, False, False]]
        matr1 = DiagonalMatrix(matrix)
        self.assertEqual(matr1.function_f8(0, 1, 2), [False, False, False, False, False,
                                                      False, False, False, False, False, False, True, False, False,
                                                      True, False])

    def test_f13(self):
        matrix = [[True, True, False, False, False, True, True, False, False, True, False, False, True, False, True,
                   True], [True, True, True, False, False, False, True, True, False, False, True, False, True, False,
                           True, False], [False, True, True, True, True, False, False, False, False, False, True, True,
                                          True, True, False, False], [True, False, True, True, True, False, False,
                                                                      False, True, False, True, False, True, True, True,
                                                                      True], [False, False, True, False, True, True,
                                                                              True, True, True, True, True, False, True,
                                                                              True, False, True], [False, True, True,
                                                                                                   True, False, True,
                                                                                                   False, False, True,
                                                                                                   False, True, True,
                                                                                                   True, True, False,
                                                                                                   False], [True, False,
                                                                                                            False, True,
                                                                                                            False,
                                                                                                            False, True,
                                                                                                            False, True,
                                                                                                            False, True,
                                                                                                            True, True,
                                                                                                            False, True,
                                                                                                            True],
                  [False, False, True, True, True, True, False, True, True, True, True, False, True, False, False,
                   True], [False, True, False, False, True, True, False, False, True, True, False, False, True, False,
                           True, True], [True, False, True, False, True, True, True, False, True, True, False, False,
                                         False, True, True, True], [False, True, False, True, True, False, False, True,
                                                                    False, False, True, True, False, False, False,
                                                                    False], [True, True, False, False, True, True,
                                                                             False, False, True, False, False, False,
                                                                             False, True, True, True], [True, False,
                                                                                                        False, True,
                                                                                                        True, False,
                                                                                                        True, False,
                                                                                                        False, False,
                                                                                                        False, False,
                                                                                                        True, True,
                                                                                                        True, False],
                  [False, False, False, True, False, False, False, False, False, True, False, False, False, False,
                   True, False], [False, False, False, False, False, True, True, False, True, False, False, True, True,
                                  True, False, False], [True, True, True, False, False, False, True, False, False,
                                                        False, True, True, True, True, False, False]]
        matr1 = DiagonalMatrix(matrix)
        self.assertEqual(matr1.function_f13(0, 1, 2), [True, True, True, False, False,
                                                       False, False, False, True, False, False, True, False, True,
                                                       True, True])

    def test_function_addition_of_fields(self):
        matrix = [[True, True, False, False, False, True, True, False, False, True, False, False, True, False, True,
                   True], [True, True, True, False, False, False, True, True, False, False, True, False, True, False,
                           True, False], [False, True, True, True, True, False, False, False, False, False, True, True,
                                          True, True, False, False], [True, False, True, True, True, False, False,
                                                                      False, True, False, True, False, True, True, True,
                                                                      True], [False, False, True, False, True, True,
                                                                              True, True, True, True, True, False, True,
                                                                              True, False, True], [False, True, True,
                                                                                                   True, False, True,
                                                                                                   False, False, True,
                                                                                                   False, True, True,
                                                                                                   True, True, False,
                                                                                                   False], [True, False,
                                                                                                            False, True,
                                                                                                            False,
                                                                                                            False, True,
                                                                                                            False, True,
                                                                                                            False, True,
                                                                                                            True, True,
                                                                                                            False, True,
                                                                                                            True],
                  [False, False, True, True, True, True, False, True, True, True, True, False, True, False, False,
                   True], [False, True, False, False, True, True, False, False, True, True, False, False, True, False,
                           True, True], [True, False, True, False, True, True, True, False, True, True, False, False,
                                         False, True, True, True], [False, True, False, True, True, False, False, True,
                                                                    False, False, True, True, False, False, False,
                                                                    False], [True, True, False, False, True, True,
                                                                             False, False, True, False, False, False,
                                                                             False, True, True, True], [True, False,
                                                                                                        False, True,
                                                                                                        True, False,
                                                                                                        True, False,
                                                                                                        False, False,
                                                                                                        False, False,
                                                                                                        True, True,
                                                                                                        True, False],
                  [False, False, False, True, False, False, False, False, False, True, False, False, False, False,
                   True, False], [False, False, False, False, False, True, True, False, True, False, False, True, True,
                                  True, False, False], [True, True, True, False, False, False, True, False, False,
                                                        False, True, True, True, True, False, False]]
        matr1 = DiagonalMatrix(matrix)
        matr1.function_addition_of_fields([1, 1, 1])
        expected_result = [[True, True, True, False, False, True, True, False, False, True, False, False, True, False,
                            True, True], [True, True, False, False, False, False, True, True, False, False, True, False,
                                          True, False, True, False], [False, True, True, True, True, False, False,
                                                                      False, False, False, True, True, True, True,
                                                                      False, False], [True, False, True, True, True,
                                                                                      False, False, False, True, False,
                                                                                      True, False, True, True, True,
                                                                                      True], [False, False, True, False,
                                                                                              True, True, True, True,
                                                                                              True, True, True, False,
                                                                                              True, True, False, True],
                           [False, True, True, True, False, True, False, False, True, False, True, True, True, True,
                            False, False], [True, False, False, True, False, False, True, False, True, False, True,
                                            True, True, False, True, True], [False, False, True, True, True, True,
                                                                             False, True, True, True, True, False, True,
                                                                             False, False, True],[False, True, False,
                                                                                                  False, True, True,
                                                                                                  False, False, True,
                                                                                                  True, False, False,
                                                                                                  True, False, True,
                                                                                                  True], [True, False,
                                                                                                          True, False,
                                                                                                          True, True,
                                                                                                          True, False,
                                                                                                          True, True,
                                                                                                          False, False,
                                                                                                          False, True,
                                                                                                          True, True],
                           [False, True, False, True, True, False, False, True, False, False, True, True, False, False,
                            False, False], [True, True, False, False, True, True, False, False, True, False, False,
                                            False, False, True, True, True], [True, False, False, True, True, False,
                                                                              True, False, False, False, False, False,
                                                                              True, True, True, False], [False, False,
                                                                                                         True, True,
                                                                                                         False, False,
                                                                                                         False, False,
                                                                                                         False, True,
                                                                                                         False, False,
                                                                                                         False, False,
                                                                                                         True, False],
                           [False, False, False, False, False, True, True, False, True, False, False, True, True, True,
                            False, False], [True, True, False, False, False, False, True, False, False, False, True,
                                            True, True, True, False, False]]
        self.assertEqual(matr1.matrix, expected_result)

    def test_interval_search(self):
        matrix = [[True, True, False, False, False, True, True, False, False, True, False, False, True, False, True,
                   True], [True, True, True, False, False, False, True, True, False, False, True, False, True, False,
                           True, False], [False, True, True, True, True, False, False, False, False, False, True, True,
                                          True, True, False, False], [True, False, True, True, True, False, False,
                                                                      False, True, False, True, False, True, True, True,
                                                                      True], [False, False, True, False, True, True,
                                                                              True, True, True, True, True, False, True,
                                                                              True, False, True], [False, True, True,
                                                                                                   True, False, True,
                                                                                                   False, False, True,
                                                                                                   False, True, True,
                                                                                                   True, True, False,
                                                                                                   False], [True, False,
                                                                                                            False, True,
                                                                                                            False,
                                                                                                            False, True,
                                                                                                            False, True,
                                                                                                            False, True,
                                                                                                            True, True,
                                                                                                            False, True,
                                                                                                            True],
                  [False, False, True, True, True, True, False, True, True, True, True, False, True, False, False,
                   True], [False, True, False, False, True, True, False, False, True, True, False, False, True, False,
                           True, True], [True, False, True, False, True, True, True, False, True, True, False, False,
                                         False, True, True, True], [False, True, False, True, True, False, False, True,
                                                                    False, False, True, True, False, False, False,
                                                                    False], [True, True, False, False, True, True,
                                                                             False, False, True, False, False, False,
                                                                             False, True, True, True], [True, False,
                                                                                                        False, True,
                                                                                                        True, False,
                                                                                                        True, False,
                                                                                                        False, False,
                                                                                                        False, False,
                                                                                                        True, True,
                                                                                                        True, False],
                  [False, False, False, True, False, False, False, False, False, True, False, False, False, False,
                   True, False], [False, False, False, False, False, True, True, False, True, False, False, True, True,
                                  True, False, False], [True, True, True, False, False, False, True, False, False,
                                                        False, True, True, True, True, False, False]]
        matr1 = DiagonalMatrix(matrix)
        smaller_bound = [0] * 16
        greater_bound = [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        matr1.interval_search(smaller_bound, greater_bound)
        expected_result = [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(matr1.interval_search(smaller_bound, greater_bound), expected_result)




if __name__ == '__main__':
    unittest.main()
