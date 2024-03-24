# R-1.1
"""write a short python function, is_multiple(n, m),
that takes two integer values and returns True if n is a multiple of m,
that is, n = mi for some integer i, and false otherwise"""

#SOLUTION:
"""
is_multiple = lambda n, m: n % m == 0
print(is_multiple(*map(int, input("Enter two integers separated by comma: ").split(', '))))

"""

#-----------------------------------------------------------------------------------------------------------
# R-1.2
"""Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators"""

#SOLUTION:
"""
iseven = lambda x: divmod(x, 2)[1] == 0
print(iseven(int(input("enter an integer: "))))
"""

#-----------------------------------------------------------------------------------------------------------
# R-1.3
"""Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution"""

#SOLUTION: we will perform a linear search
"""
def minmax(data):
    if not data: #if the list/array is empty
        return None, None

    min_value = max_value = data[0]  #initializing both with the first element of the array

    for i in data[1:]:   #start the iteration with the second element of the array
        if i < min_value:
            min_value = i
        elif i > max_value:
            max_value = i
    return min_value, max_value

print(minmax(list(map(int, input("enter a list of integers seperated by commas: ").split(',')))))
"""

#-----------------------------------------------------------------------------------------------------------
# R-1.4
"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n."""

#SOLUTION:
"""
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n))

# Example usage:
print(sum_of_squares(int(input("Enter a positive integer: "))))

"""

#-----------------------------------------------------------------------------------------------------------
# R-1.5
"""Give a single command that computes the sum from
 Exercise R-1.4, relying on Python’s comprehension syntax 
 and the built-in sum function."""

#SOLUTION:
"""
print(sum(i ** 2 for i in range(1, int(input("enter an integer: ")))))
"""
#-----------------------------------------------------------------------------------------------------------
# R-1.6
"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n"""

#SOLUTION:
"""
print(sum(i ** 2 for i in range(1, int(input("Enter an integer: "))) if i % 2 != 0))
"""

#-----------------------------------------------------------------------------------------------------------
# R-1.7
"""Give a single command that computes the sum from Exercise R-1.6,
 relying on Python’s comprehension syntax and the built-in sum function."""
#SOLUTION:
"""
print(sum(i ** 2 for i in range(1, int(input("Enter an integer: "))) if i % 2 != 0))
"""

#-----------------------------------------------------------------------------------------------------------
# R-1.8
"""Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent
index j ≥ 0 such that s[j] references the same element?"""

# SOLUTION is that j = len(s) + k
"""
s = input("Enter your string: ")
k = int(input("Enter the negative index: ")); k = k if k < 0 else int(input("You entered a positive index. Please enter a negative index: "))
j = len(s) + k
print(f"The positive index equivalent to your provided negative index is: {j}")
"""

#-----------------------------------------------------------------------------------------------------------
# R-1.9
"""9 What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?"""

#SOLUTION
"""
for i in range(50, 90, 10):
    print(i)
"""

#-----------------------------------------------------------------------------------------------------------
# R-1.10
"""What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?"""

#SOLUTION
"""
for i in range(8, -10, -2):
    print(i)
"""

#-----------------------------------------------------------------------------------------------------------
# R-1.11
"""Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256]."""

#SOLUTION
#SYNTAX for list comprehension: expression for value in iterable if condition
"""
result_list = [2 ** i for i in range(9)]
print(result_list)
"""



#-----------------------------------------------------------------------------------------------------------
# R-1.12
"""Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function"""

import random

s = list(map(str, input("enter a list of items you like: ").split(", ")))
my_choice = lambda s: s[random.randrange(len(s))]
print("randomly selected item using my choice: ", my_choice(s))


#-----------------------------------------------------------------------------------------------------------
