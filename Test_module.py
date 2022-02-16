import unittest

from numpy import true_divide
from arithmetic_arranger import arithmatic_arranger

class UnitTests(unittest.TestCase):
    def test_arrangement(self):
        actual = arithmatic_arranger(
            ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
        self.assertEqual(
            actual, expected,
            'Expected different output when calling "arithmetic_arranger()" with ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]'
        )

        actual = arithmatic_arranger(
            ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected =   "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
        self.assertEqual(
            actual, expected,
            'Expected different output when calling "arithmetic_arranger()" with ["7 + 12", "8967 - 2677", "2 + 78", "74 + 56", "32 - 9"]'
        )

    def test_too_many_problems(self):
        actual = arithmatic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "12 + 40","445 + 4578"])
        expected = "Error: Too many problems."
        self.assertEqual(
            actual, expected,
            'Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many problems."'
        )

    def test_incorrect_operator(self):
        actual = arithmatic_arranger(
            ["3 * 2355", "38 - 2", "4533 + 423", "3 + 49"])
        expected = "Error: Operator must be '+' or '-'."
        self.assertEqual(
            actual, expected,
            '''Expected calling "arithmetic_arranger()" with a problem that uses the "/" operator to return "Error: Operator must be '+' or '-'."'''
        )

    def test_too_many_digits(self):
        actual = arithmatic_arranger(
            ["24333443 + 875", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers cannot be more than four digits."
        self.assertEqual(
            actual, expected,
            'Expected calling "arithmetic_arranger()" with a problem that has a number over 4 digits long to return "Error: Numbers cannot be more than four digits."'
        )

    def test_only_digits(self):
        actual = arithmatic_arranger(
            ["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers must only contain digits."
        self.assertEqual(
            actual, expected,
            'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."'
        )

    def test_solutions(self):
        actual = arithmatic_arranger(
            ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
        expected = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"
        self.assertEqual(
            actual, expected,
            'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with arithemetic problems and a second argument of `True`.'
        )


if __name__ == "__main__":
    unittest.main()
        