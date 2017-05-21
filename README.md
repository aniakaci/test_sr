## Instructions

The following problems can be solved by any mean of your choice, although javascript is preferred for simplicity. 
Your answer should consists of a github repo link with your code if you wrote any, a README.md explaining how to run your code, giving your numerical answers and all explanations that you deemed adequate.
Bear in mind, we are more interested in your reasoning and coding than in your numerical answer. Even if you didn't get to an answer for a problem, we are still interested in your attempt.

Feel free to add anything that you deem of interest (first ideas of solutions that did/didnt work, performance benchmarks... )
Finaly, keep streamroot name out of the repository as it is a registered trademark.


## Problems

Problem 1 is mandatory.
You can pick one or more of problem 2,3 and 4. 
You are of course allowed to answer them all :)


### Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 10000.


### Problem 2

A k-input binary truth table is a map from k input bits (binary digits, 0 [false] or 1 [true]) to 1 output bit. For example, the 2-input binary truth tables for the logical AND and XOR functions are:

x  | y | x AND y
0  | 0 |   0
0  | 1 |   0
1  | 0 |   0
1  | 1 |   1


x  |  y  | x XOR y
0  |  0  |    0
0  |  1  |    1
1  |  0  |    1
1  |  1  |    0

How many 6-input binary truth tables, τ, satisfy the formula

τ(a, b, c, d, e, f) AND τ(b, c, d, e, f, a XOR (b AND c)) = 0

for all 6-bit inputs (a, b, c, d, e, f)?


### Problem 3

Given an ordered set of digits (a_1, a_2, ... , a_n) and a number N, build expressions by inserting "+"
or "-" anywhere between the digits (a_1, .., a_n) so that it results to the number N.

Your method should return all possible expressions resulting to the number N for any (a_1, a_2, ... a_n)


Example with N = 100 and (a_1, ..., a_n) = (1,2,3,4,5,6,7,8,9) :

123 - 45 - 67 + 89 = 100
12 - 3 - 4 + 5 - 6 + 7 + 89 = 100
12 + 3 + 4 + 5 - 6 - 7 + 89 = 100
123 + 4 - 5 + 67 - 89 = 100
1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 = 100
12 + 3 - 4 + 5 + 67 + 8 + 9 = 100
1 + 23 - 4 + 56 + 7 + 8 + 9 = 100
1 + 2 + 34 - 5 + 67 - 8 + 9 = 100
1 + 23 - 4 + 5 + 6 + 78 - 9 = 100
123 + 45 - 67 + 8 - 9 = 100
123 - 4 - 5 - 6 - 7 + 8 - 9 = 100


### Problem 4

Design a queuing system. The queue should implement add, view and delete. A
viewed message will be invisible to other workers for five seconds unless it is
deleted. Messages should be returned in order they were added unless they have
been deleted.

The add method takes a string as a message and returns a unique id for that
message.  The view method takes no parameters and returns a hash containing the
next message and the unique message id assigned in the add method.  The delete
method takes the unique message id and returns true if the message was removed
within 5 seconds or false if we were too slow.

Extra points: Do you see any problems with running this kind of queue in a
production envrionment?
