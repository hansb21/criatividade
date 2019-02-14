'''Module for tokenizing strings into components of arithmetic expressions.'''

import re

from calc.operators import make_operator

REGEXES = [
    (re.compile(r'\s+'), lambda _: None),
    (re.compile(r'(\+|-)?([1-9]\d*|0)\.\d*'), float),
    (re.compile(r'(\+|-)?[1-9]\d*'), int),
    (re.compile(r'\+'), make_operator)
]


def tokenize(string):
    '''Make a stream of tokens from a string.

    Args:
        string (str): the string to tokenize

    Yields:
        token: tokens from the string
    '''
    position = 0

    while position < len(string):
        for regex, token_type in REGEXES:
            match = regex.match(string, position)
            if match is not None:
                begin, end = match.span()
                token = token_type(string[begin:end])
                if token:
                    yield token
                position = end
                break
        else:
            raise ValueError('Bad token')
