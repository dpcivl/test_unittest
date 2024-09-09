"""
###단위 테스트 목표###
1. add 메서드가 두 수를 더하는지 확인
2. subtarct 메서드가 두 수를 정확히 빼는지 확인
3. multiply 메서드가 두 수를 정확히 곱하는지 확인
4. divide 메서드가 두 수를 정확히 나누는지 확인
5. divide 메서드가 0으로 나누는 경우 ValueError를 발생시키는지 확인
"""

import unittest
import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator.Calculator()

    def test_add(self):
        a = 3
        b = 5

        res = self.calc.add(a,b)

        self.assertEqual(res, 8)

    def test_subtract(self):
        a = 5
        b = 3

        res = self.calc.subtract(a,b)

        self.assertEqual(res, 2)

    def test_multiply(self):
        a = 3
        b = 5

        res = self.calc.multiply(a,b)

        self.assertEqual(res, 15)

    def test_divide(self):
        a = 6
        b = 3

        res = self.calc.divide(a,b)

        self.assertEqual(res, 2)

    def test_divide_WhenDividedByZero(self):
        a = 6
        b = 0

        # res = self.calc.divide(a,b)

        # self.assertRaises(ValueError, self.calc.divide, a, b)

        with self.assertRaises(ValueError):
            self.calc.divide(a, b)

    def test_power(self):
        a = 3
        b = 2

        res = self.calc.power(a, b)

        self.assertEqual(res, 9)

    def test_sqrt(self):
        a = 81

        res = self.calc.sqrt(a)

        self.assertEqual(res, 9)

    def test_sqrt_WhenNegative(self):
        a = -3

        with self.assertRaises(ValueError):
            self.calc.sqrt(a)