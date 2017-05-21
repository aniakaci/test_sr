# ### Problem 3
#
# Given an ordered set of digits (a_1, a_2, ... , a_n) and a number N, build expressions by inserting "+"
# or "-" anywhere between the digits (a_1, .., a_n) so that it results to the number N.
#
# Your method should return all possible expressions resulting to the number N for any (a_1, a_2, ... a_n)
#
# Example with N = 100 and (a_1, ..., a_n) = (1,2,3,4,5,6,7,8,9) :
#
# 123 - 45 - 67 + 89 = 100
# 12 - 3 - 4 + 5 - 6 + 7 + 89 = 100
# 12 + 3 + 4 + 5 - 6 - 7 + 89 = 100
# 123 + 4 - 5 + 67 - 89 = 100
# 1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 = 100
# 12 + 3 - 4 + 5 + 67 + 8 + 9 = 100
# 1 + 23 - 4 + 56 + 7 + 8 + 9 = 100
# 1 + 2 + 34 - 5 + 67 - 8 + 9 = 100
# 1 + 23 - 4 + 5 + 6 + 78 - 9 = 100
# 123 + 45 - 67 + 8 - 9 = 100
# 123 - 4 - 5 - 6 - 7 + 8 - 9 = 100


# TODO evals

suffixes = ['', '+', '-']
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = 100

res = []


def recursive_eval(digits, suffixes, prefix="", index=0):
    """
    Recursive evaluation function that generates all the possible expressions given the digits and the suffixes to uses.
    Expression That are equal to 'N' are added in the global list 'res'
    :param digits: The digits to use in the expressions
    :param suffixes: The suffixes to use after each digit
    :param prefix: The recursive definition of a possible expression
    :param index: The position on the digits list to know which digits have not been added in the possible expressions
    """
    if len(digits) > index:
        s = str(digits[index])
        recursive_eval(digits, suffixes, prefix + s, index + 1)
        if len(digits) > index + 1:
            recursive_eval(digits, suffixes, prefix + s + "+", index + 1)
            recursive_eval(digits, suffixes, prefix + s + "-", index + 1)
    else:
        expression = prefix + "==" + str(N)
        if eval(expression):
            global res
            res += [expression]


recursive_eval(digits, suffixes)
print "for digits {0}, expressions {1}, and N equal to {2}," \
      " the possible expressions are:\n".format(digits, suffixes, N)
print '\n'.join(res)
