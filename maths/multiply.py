def multiply_nums(*args):
    """Multiply numbers together.

    :param args: One or more numbers to multiply.
    :type args: float
    :returns: The product of all numbers provided.
    :rtype: float

    Example::
        >>> multiply_nums(2, 3, 4)
        24
    """
    mult = 1
    for n in args:
        mult = mult * n
    return mult