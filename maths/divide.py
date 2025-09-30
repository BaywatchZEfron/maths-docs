def divide_nums(*args):
    """Divide numbers in sequence.

    The first number is taken as the starting point,
    and all following numbers divide the current result.

    :param args: Two or more numbers to divide.
    :type args: float
    :returns: The result of sequential division.
    :rtype: float

    Example::
        >>> divide_nums(100, 2, 5)
        10.0
    """
    div = args[0]
    for n in args[1:]:
        div = div / n
    return div
