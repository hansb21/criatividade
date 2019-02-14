'''Tests for the calc.tokenize module'''
from unittest import TestCase

from calc.tokenize import make_operator, tokenize


class TokenizeTest(TestCase):
    '''Test fixture for the calc.tokenize module'''
    def assert_tokenize(self, string, tokens):
        '''Check tokenizing is done as expected'''
        expected = list(tokenize(string))
        self.assertEqual(expected, tokens)

    def test_make_operator_add(self):
        '''Addition operator should add'''
        stack = [4, 2]
        operator = make_operator('+')
        operator(stack)
        self.assertEqual(stack.pop(), 6)

    def test_make_operator_subtract(self):
        '''Subtraction operator should add'''
        stack = [4, 2]
        operator = make_operator('-')
        operator(stack)
        self.assertEqual(stack.pop(), 2)

    def test_tokenize_empty(self):
        '''Empty string gives no tokens'''
        self.assert_tokenize('', [])

    def test_tokenize_integer(self):
        '''A single integer gives a single integer'''
        self.assert_tokenize('42', [42])

    def test_tokenize_float(self):
        '''A single float gives a single float'''
        self.assert_tokenize('42.42', [42.42])

    def test_tokenize_with_operator(self):
        '''Tokenizes operators correctly'''
        self.assert_tokenize('+', [make_operator('+')])

    def test_tokenize_addition(self):
        '''Tokenizes a rpn addition'''
        self.assert_tokenize('4 2 +', [4, 2, make_operator('+')])

    def test_tokenize_subtraction(self):
        '''Tokenizes a rpn subtraction'''
        self.assert_tokenize('4 2 -', [4, 2, make_operator('-')])

    def test_tokenize_raises_bad_token(self):
        '''Raises exception on wrong token'''
        with self.assertRaises(ValueError):
            list(tokenize('not-a-token'))
