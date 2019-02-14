'''Tests for the rpn module'''
from unittest import TestCase

from calc.tokenize import make_operator
from calc.rpn import execute


class RPNTest(TestCase):
    '''Test fixture for the rpn module'''
    def assert_execute(self, tokens, result):
        '''Test execution of a sequence of tokens'''
        self.assertEqual(execute(tokens), result)

    def test_execute_single_value(self):
        '''Should simply return a single value'''
        self.assert_execute([42.42], 42.42)

    def test_return_top_value(self):
        '''Should return the last value pushed'''
        self.assert_execute([4, 2, 42.42, 42], 42)

    def test_execute_addition(self):
        '''Should execute an addition correctly'''
        self.assert_execute([4, 2, make_operator('+')], 6)

    def test_execute_multiplication(self):
        '''Should execute a multiplication correctly'''
        self.assert_execute([4, 2, make_operator('*')], 8)
