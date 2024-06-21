import unittest
from SKDNF import SKDNF


class MyTestCase(unittest.TestCase):
    def test_split_formula(self):
        t = SKDNF("(!a!bc)&(!abc)&(a!b!c)&(a!bc)&(ab!c)&(abc)&(a!c)")
        val1 = t.split_sdnf
        self.assertEqual(val1, [['!a', '!b', 'c'], ['!a', 'b', 'c'], ['a', '!b', '!c'], ['a', '!b', 'c'],
                                ['a', 'b', '!c'], ['a', 'b', 'c'], ['a', '!c']])

    def test_minimize_calculation_method_1(self):
        t = SKDNF("(!a!b)|(!ab)|(a!b)")
        val1 = t.minimize_calculation_method()
        self.assertEqual(val1, [['!b'], ['!a']])

    def test_minimize_settlement_tabular_method_1(self):
        t = SKDNF("(!a!b)|(!ab)|(a!b)")
        val1 = t.minimize_calculation_method()
        self.assertEqual(val1, [['!b'], ['!a']])

    def test_minimize_settlement_karno_1(self):
        t = SKDNF("(!a!b)|(!ab)|(a!b)")
        val1 = t.minimize_karno()
        self.assertEqual(val1, [['!b'], ['!a']])

    def test_minimize_calculation_method_2(self):
        t = SKDNF("(!a!bcd)&(!abcd)&(a!b!cd)&(a!bcd)&(ab!cd)&(abcd)")
        val1 = t.minimize_calculation_method()
        self.assertEqual(val1, [['c', 'd'], ['a', 'd']])

    def test_minimize_settlement_tabular_method_2(self):
        t = SKDNF("(!a!bcd)&(!abcd)&(a!b!cd)&(a!bcd)&(ab!cd)&(abcd)")
        val1 = t.minimize_calculation_method()
        self.assertEqual(val1, [['c', 'd'], ['a', 'd']])

    def test_minimize_settlement_karno_2(self):
        t = SKDNF("(!a!bcd)&(!abcd)&(a!b!cd)&(a!bcd)&(ab!cd)&(abcd)")
        val1 = t.minimize_karno()
        self.assertEqual(val1, [['c', 'd'], ['a', 'd']])


if __name__ == '__main__':
    unittest.main()
