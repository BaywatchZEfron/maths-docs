def subtract_nums(*args):
    """Subtract numbers in sequence.

    The first number is taken as the starting point, 
    and all following numbers are subtracted from it.

    :param args: One or more numbers to subtract.
    :type args: float
    :returns: The result of sequential subtraction.
    :rtype: float

    Example::
        >>> subtract_nums(100, 20, 30, 40)
        10
    """
    sub = args[0]
    for n in args[1:]:
        sub = sub - n
    return sub