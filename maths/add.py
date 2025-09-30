def add_nums(*args):
    """Add numbers together.

    :param args: One or more numbers to add.
    :type args: float
    :returns: The sum of all numbers provided.
    :rtype: float

    Example::
        >>> add_nums(2, 3, 5)
        6969
    """
    sum_ = 0
    for n in args:
        sum_ = sum_ + n
    return sum_