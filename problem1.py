# ### Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 10000.
from math import log, log10


# TODO
# multiples_to_find_pb1 = [3, 5]
# max_value_pb1 = 10000


def sum_arithmetic_suite(u_0, r, n):
    """
    The arithmetic suite u_i is written as : u_i = u_0 * r*i
    :param u_0: The first value of the arithmetic suite
    :param r: The common difference
    :param n: The maximum index of the suite
    :return: The sum of the arithmetic suite from u_0 to u_n
    """
    return (n + 1) * (2 * u_0 + n * r) / 2


def sum_multiples(multiple_to_find, max_value):
    """

    :param multiple_to_find: The value for we which we want to find the sum of multiples
    :param max_value: The maximum value of a multiple to find (multiples must be strictly less than this value)
    :return: The sum of all multiples of multiple_to_find less than max_value
    """
    last_multiple = (max_value - 1) - ((max_value - 1) % multiple_to_find)
    n = last_multiple / multiple_to_find
    return sum_arithmetic_suite(0, multiple_to_find, n)


# print sum_multiples(3,10)+sum_multiples(5,10) #23
print "Sum of multiples of 5 and 3 lower than 10000 is equal to : {0}".format(
    sum_multiples(3, 10000) + sum_multiples(5, 10000))  # 26663333
