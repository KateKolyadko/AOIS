import unittest
from TtruthTable import TruthTable


class TestTruthTable(unittest.TestCase):
    def test_determine_value(self):
        t = TruthTable("")
        self.assertEqual(t.determine_value("(0->0)"), 1)
        self.assertEqual(t.determine_value("(1->0)"), 0)
        self.assertEqual(t.determine_value("(0&0)"), 0)
        self.assertEqual(t.determine_value("(0&1)"), 0)
        self.assertEqual(t.determine_value("(1&0)"), 0)
        self.assertEqual(t.determine_value("(1&1)"), 1)
        self.assertEqual(t.determine_value("(0|0)"), 0)
        self.assertEqual(t.determine_value("(0|1)"), 1)
        self.assertEqual(t.determine_value("(1|0)"), 1)
        self.assertEqual(t.determine_value("(1|1)"), 1)
        self.assertEqual(t.determine_value("(0~0)"), 1)
        self.assertEqual(t.determine_value("(1~1)"), 1)
        self.assertEqual(t.determine_value("!0"), 1)
        self.assertEqual(t.determine_value("!1"), 0)

    def test_table(self):
        t = TruthTable("(a->b)")
        expected_value = [['0', '0', '1'], ['0', '1', '1'], ['1', '0', '0'], ['1', '1', '1']]
        self.assertEqual(expected_value, t.table)

    def test_sknf(self):
        t = TruthTable("(a~b)")
        expected_value_1 = "(a|!b)&(!a|b)"
        expected_value_2 = "(1, 2) &"
        actual_value_1, actual_value_2 = t.create_sknf()
        self.assertEqual(expected_value_1, actual_value_1)
        self.assertEqual(expected_value_2, actual_value_2)

    def test_sdnf(self):
        t = TruthTable("((a&b)->a)")
        expected_value_1 = "(!a&!b)|(!a&b)|(a&!b)|(a&b)"
        expected_value_2 = "(0, 1, 2, 3) |"
        actual_value_1, actual_value_2 = t.create_sdnf()
        self.assertEqual(expected_value_1, actual_value_1)
        self.assertEqual(expected_value_2, actual_value_2)

    def test_index_form(self):
        t = TruthTable("((a&b)|a)")
        expected_value_1 = 3
        expected_value_2 = ['0', '0', '1', '1']
        actual_value_1, actual_value_2 = t.create_index_form()
        self.assertEqual(expected_value_1, actual_value_1)
        self.assertEqual(expected_value_2, actual_value_2)


if __name__ == '__main__':
    unittest.main()
