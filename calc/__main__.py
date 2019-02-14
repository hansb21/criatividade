'''Main module for the calculator.'''
import sys

from readline import parse_and_bind

from calc.rpn import execute
from calc.tokenize import tokenize

parse_and_bind('')


def run():
    '''Run the program.'''
    while True:
        try:
            string = input('>>> ')
        except EOFError:
            print()
            exit()
        try:
            print(execute(tokenize(string)))
        except ValueError as exc:
            print(exc, file=sys.stderr)
        except IndexError as exc:
            print(exc, file=sys.stderr)


if __name__ == '__main__':
    run()
