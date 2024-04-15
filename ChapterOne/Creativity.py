#C-1.13
"""Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing"""
#import numpy as np

#SOLUTION
#pseudo-code
"""
function reverse_list(list):
    n = length of list
    left = 0
    right = n -1 
    while left<right:
        swap list[left] with list[right]
        left = left +1 
        right = right -1

#python code
def reverse_list(list):
    return list[::-1]
list = [1, 2, 3, 4, 5]
print(reverse_list(list))
"""
#-------------------------------------------------------------------------

#C-1.14
"""Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd."""
"""
def distinctoddpairgen(array):
    for num1 in array:
        for num2 in array:
            if num1 != num2 and (num1 * num2) % 2 == 1:
                yield (num1, num2)


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gen = distinctoddpairgen(data)

print('Generator Solution')
for item in gen:
    print(item)
"""
"""

# Any two odd numbers will produce an odd product.  O(n)
def determineoddpair(array):
    first_odd = None
    for number in array:
        if number % 2 == 1:
            if number != first_odd and not first_odd is None:
                return ('True', first_odd, number)
            else:
                first_odd = number
    return ('Not found')


data = [2, 4]
determineoddpair(data)
"""
#-------------------------------------------------------------------------

#C-1.15
"""Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct)."""
"""

SOLUTION: 
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [1, 2, 2, 4, 5, 6, 7, 7]

def distinct(n):
    my_set = set(n)
    if len(n) == len(my_set):
        return "distinct"
    else:
        return "not distinct"

print(distinct(a))
print(distinct(b))
"""
#-------------------------------------------------------------------------

#C-1.16
"""Question: In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] = factor. We have discussed that numeric
types are immutable, and that use of the = operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?

Answer:
The reason why the actual parameter sent by the caller is changed 
despite the immutability of numeric types lies in the behavior of lists in Python.
In the scale function, `data` is a list of numeric values.
When you perform `data[j] = factor` within the loop, you are not modifying
the numeric value itself, but rather you are modifying
the list `data` at the index `j` to reference a new object.

So, while the individual numeric values in the list `data` remain immutable,
the list `data` itself is mutable, and by assigning a new value to `data[j]`,
you are effectively changing the content of the list. Therefore, the changes 
made within the `scale` function are reflected in the original list passed as 
an argument to the function.
"""
#-------------------------------------------------------------------------

#C-1.17
"""Question: Had we implemented the scale function (page 25) as follows, does it work
properly?
def scale(data, factor):
for val in data:
val = factor
Explain why or why not.

Answer: 
The variable val is simply a local variable that takes on the value of factor
in each iteration of the loop. However, this does not modify the elements of 
the list data. Instead, it rebinds the local variable val in each iteration, 
which has no effect on the elements of data outside of the loo.
"""
#-------------------------------------------------------------------------

#C-1.18
"""Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

SOLUTION:
my_list = [i + (i*i) for i in range(0, 10)]
print(my_list)
"""
#-------------------------------------------------------------------------

#C-1.19
"""Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.

my_alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(my_alphabet)
"""
#-------------------------------------------------------------------------

#C-1.20
"""Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible order occurs with
equal probability. The random module includes a more basic function randint(a, b) that 
returns a uniformly random integer from a to b (including both endpoints). 
Using only the randint function,implement your own version of the shuffle function.

import random

my_list = [1, 2, 3, 4, 5, 8, 2, 0, 199, 433, 65, 2, 56, 72, -1, -766]

def using_randint(my_list):
    list_len = len(my_list)
    for item in range(list_len):
        j = random.randint(0, item)
        my_list[item], my_list[j] = my_list[j], my_list[item]
using_randint(my_list)
print(my_list)

"""
#-------------------------------------------------------------------------

#C-1.21
"""Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D)

user_input = []
try:
    while True:
        line = input("Enter your input and press Ctrl-D to end: \n")
        user_input.append(line)
except EOFError:
        print("Input ended. Printing lines in reverse order:")
        for line in reversed(user_input):
            print(line)

"""
#-------------------------------------------------------------------------


#C-1.22
"""Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.

#SOLUTION ONE USING THE NUMPY DOT OPERATOR:
array_a = list(map(int, input("Enter the first array separated by commas: ").split(",")))
array_b = list(map(int, input("Enter the second array separated by commas: ").split(",")))
if len(array_b) != len(array_a):
    print("Both arrays need to have equal length!")
else:
    dot_product = np.dot(array_a, array_b)
    print(dot_product)
#--------------------------------------------------------------------------------------------
#SOLUTION TWO USING LOOPS:
array_a = list(map(int, input("Enter the first array separated by commas: ").split(",")))
array_b = list(map(int, input("Enter the second array separated by commas: ").split(",")))
if len(array_b) != len(array_a):
    print("Both arrays need to have equal length!")
else:
    dot_product_result = 0
    for i in range(len(array_a)):
        dot_product_result += array_a[i] * array_b[i]
    print(dot_product_result)
"""
#-------------------------------------------------------------------------

#C-1.23
"""Give an example of a Python code fragment that attempts to write an element to a
list based on an index that may be out of bounds.
If that index is out of bounds, the program should catch the exception that results, and
print the following error message: “Don’t try buffer overflow attacks in Python!”

#SOLUTION-:

list_a = [1, 2, 3, 4, 5]
b = 5
index_b = 19

if index_b < 0 or index_b > len(list_a):
    raise IndexError("Don’t try buffer overflow attacks in Python!")
else:
    list_a.insert(index_b, b)
    print(list_a)
"""
#-------------------------------------------------------------------------------

#C-1.24
"""Write a short Python function that counts the number of vowels in a given
character string.

#SOLUTION:

def count_vowels(str):
    vowels = "aeiouAEIOU"
    count = 0
    for char in str_a:
        if char in vowels:
            count += 1
    return count


str_a = "Hey what is your name?"
print(count_vowels(str_a))
"""
#---------------------------------------------------------------------------------------------

#C-1.25
"""Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. 
For example, if given the string "Let s try, Mike.", this function would return
"Lets try Mike".

#SOLUTION USING STRING:TRANSLATE89 METHOD:

import string

def remove_punctuation(s):
    translator = str.maketrans('', '', string.punctuation) # Create a translation table to remove punctuation
    return s.translate(translator) # Translate characters in the input string using the translation table

s = input("enter a sentence. ")
result = remove_punctuation(s)
print(result)

#--------------------------------------------------------------------------------------------

# SOLUTION USING MANUAL ITERATION:

import string

def remove_punctuation(s):
    punctuation_chars = string.punctuation
    # ''.join() is calling the join() method on an empty string
    return ''.join(char for char in s if char not in punctuation_chars)

# Example usage:
s = "Hello, World! This is a test."
result = remove_punctuation(s)
print(result)

#--------------------------------------------------------------------------------
#SOLUTION USING REGEX (REGULAR EXPRESSIONS).

import re

def remove_punctuation(s):
    return re.sub('r'[^\w\s]', '', s)
    # re.sub(): This function is used to replace substrings
    # that match a specified pattern with a new substring.
    # 'r'[^\w\s]': This regular expression pattern matches any character
    # that is not a word character (#\w) or whitespace character (\s).
    # The ^ inside the square brackets [] denotes negation,
    # meaning it matches any character not specified in the pattern.

# Example usage:
s = "Hello, World! This is a test."
result = remove_punctuation(s)
print(result)

"""
# ----------------------------------------------------------------------------------------------
#C-1.26

"""Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”
def checkFormula(a, b, c):
    if a + b == c:
        return True, f"{a} + {b} = {c}"
    elif a == b - c:
        return True, f"{a} = {b} - {c}"
    elif a * b == c:
        return True, f"{a} * {b} = {c}"
    else:
        return False, "No valid arithmetic formula found. "

print("Enter a number and press enter: ")
a, b, c = [int(input(f"number {i+1}: ")) for i in range(3)]
print(checkFormula(a, b, c))
"""
#----------------------------------------------------------------------------------------------

#C-1.27
"""In Section 1.8, we provided three different implementations of a generator
that computes factors of a given integer. The third of those implementations,
from page 41, was the most efficient, but we noted that it did not
yield the factors in increasing order. Modify the generator so that it reports
factors in increasing order, while maintaining its general performance advantages."""

#-----------------------------------------------------------------------------------------------

#C-1.29
"""Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once."""

#------------------------------------------------------------------------------------------------

#C-1.30
"""Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2."""

#-------------------------------------------------------------------------------------------------

#C-1.31
"""Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible."""

#C-1.32
"""Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator"""

#C-1.33
"""Write a Python program that simulates a handheld calculator. Your program should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each operation is performed. Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation."""

#C-1.34
"""A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos"""

#C-1.35
"""The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20,...,100"""

#C-1.36
"""Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book.
"""