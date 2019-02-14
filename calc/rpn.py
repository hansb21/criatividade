'''Module implementing a reverse polish notation calculator'''


def execute(tokens):
    '''Execute operations according to a sequence of tokens

    Args:
        tokens (sequence): a sequence of tokens

    Returns:
        object: the result of the sequence of operations
    '''
    stack = []

    for token in tokens:
        if callable(token):
            token(stack)
        else:
            stack.append(token)

    return stack.pop()
