# ### Problem 2
#
# A k-input binary truth table is a map from k input bits (binary digits, 0 [false] or 1 [true]) to 1 output bit. For example, the 2-input binary truth tables for the logical AND and XOR functions are:
#
# x  | y | x AND y
# 0  | 0 |   0
# 0  | 1 |   0
# 1  | 0 |   0
# 1  | 1 |   1
#
#
# x  |  y  | x XOR y = not(x and y) and (x or y)
# 0  |  0  |    0
# 0  |  1  |    1
# 1  |  0  |    1
# 1  |  1  |    0
#
# How many 6-input binary truth tables, tau, satisfy the formula
#
# clause : tau(a, b, c, d, e, f) AND tau(b, c, d, e, f, a XOR (b AND c)) = 0
#
# for all 6-bit inputs (a, b, c, d, e, f)?

# a AND b = 0 <==> not(a) OR not(b) = 1
# a AND b = 1
# card(a AND b = 0) = 2^n - card(A AND b = 1)

# The opposite clause is: tau(a, b, c, d, e, f) OR tau(b, c, d, e, f, a XOR (b AND c)) = 0

# for a 6-input binary, there exist 2**6 possible values in the truth table
# a  |  b | ta1(a,b)| ta2(a,b)| tau(a,b)| tau(a,b)| tau(a,b)
# 0  |  0 |   0     |   0     |   0     |   0     |   1
# 0  |  1 |   0     |   0     |   0     |   1     |   1
# 1  |  0 |   0     |   0     |   1     |   1     |   1
# 1  |  1 |   0     |   1     |   1     |   1     |   1

# 2^n point dans mon espace 2^(2^n)= 2^(n+1)
# tau(not a, not b, not c, not d, not e, not f) AND tau(not b, not c, not d, not e, not f, a XOR (b AND c)) = 0

def AND(x, y):
    return x and y


def XOR(x, y):
    return (x and not y) or (not x and y)


def gen_truth_table(size, truths=[]):
    if not size:
        global truth_tables
        truth_tables += [truths]
    else:
        for i in [True, False]:
            gen_truth_table(size - 1, truths + [i])


def gen_func_bool(truth_tables):
    res = []
    for line in gen_truth_table(size):
        res += [lzm]
    return res





truth_tables = []
gen_truth_table(6)

print len(truth_tables)
print truth_tables
