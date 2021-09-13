# Solving using recursion
# print(x % 10)
# print(x // 10 // 10 // 10)
from itertools import dropwhile


def lstrip(iterable, pred):
    """Yield the items from *iterable*, but strip any from the beginning
    for which *pred* returns ``True``.

    For example, to remove a set of items from the start of an iterable:

        >>> iterable = (None, False, None, 1, 2, None, 3, False, None)
        >>> pred = lambda x: x in {None, False, ''}
        >>> list(lstrip(iterable, pred))
        [1, 2, None, 3, False, None]

    This function is analogous to to :func:`str.lstrip`, and is essentially
    an wrapper for :func:`itertools.dropwhile`.

    """
    return dropwhile(pred, iterable)


def reverse_number(x):
    new_num = ""
    negative = False
    if x == 0:
        return x
    while x != 0:
        if x < 0:
            negative = True
            x = -x
        new_num += str(x % 10)
        x //= 10
    # Strip leading zeroes
    new_num = str(int(new_num))
    # Convert negative
    if negative:
        new_num = -int(new_num)

    return new_num


x = 0
res = reverse_number(x)
print(res)
