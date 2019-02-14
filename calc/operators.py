'''Module for defining operators for a calculator'''


def binary(operation):
    '''Create a binary operation over a stack from a binary function

    Args:
        operation (function): a binary function over elements in the stack

    Returns:
        function: a function that executes the binary operation over the stack
    '''
    def operate(stack):
        '''Execute a binary operation on a stack.'''
        rhs = stack.pop()
        lhs = stack.pop()
        stack.append(operation(lhs, rhs))
    return operate


OPERATORS = {
    '+': binary(lambda a, b: a + b),
    '-': binary(lambda a, b: a - b),
}


def make_operator(operator):
    '''Get an operator based on its string representation.

    Args:
        operator (str): the string representation

    Returns:
        function: a function over a stack
    '''
    return OPERATORS[operator]
