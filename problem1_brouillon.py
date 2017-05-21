# ### Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 10000.
from math import log, log10

multiples_to_find_pb1 = [3, 5]
max_value_pb1 = 10000


def sum_geometric_serie(scale_factor, common_ratio, max_index):
    """
    The geometric suite gs_i is written as : gs_i = scale_factor * common_ratio**i
    :param scale_factor: 
    :param common_ratio: 
    :param max_index: 
    :return: The sum of the geomtric suite
    """
    return scale_factor * (1 - common_ratio ^ max_index) / (1 - common_ratio)


def sum_multiples(multiple_to_find, max_value):
    res_sum = 0
    i = 1
    while True:
        multiple_to_find_i = multiple_to_find * i
        if (multiple_to_find_i>=max_value):
            break
        res_sum +=multiple_to_find_i
        i = i+1
    print i
    return res_sum

print sum_multiples(3,10000)+sum_multiples(5,10000)
#
# print 10000%3 9999

# print log(9995,10)/log(5,10)
# print 5**5.72239548713
# print 5**6
#
# multiple 5: 5 10 15 20 25
# 5**i      : 5          25
# i         : 1          2

# 5^n = 9995
# exp(n ln(5)) = 9995
# n * ln(5) = ln(9995)
# n = ln(9995)/ln(5)
# n = log10(995)/log10(5)
