# sample code modified by jhun baclaan
# d.o.c. (date of creation): jan. 15, 2026

# Some Foundational Python: lists, slicing, matplotlib, numpy arrays

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import collections as matcoll

# """"""""""""""""""""
# A0-Part-1: lists
# """"""""""""""""""""

# create a list of the squares of integers from 1 to 5, and print the list
# nothing to do for this, it's already done. 
squares  = [1, 4, 9, 16, 25]
print ("full list of squares:", squares)

# print the square at index 2
# your code here
print("square at index 2:", squares[2])

# append the square of 6 to the list and print the updated list
# your code here
squares.append(36)
print("full list of squares with 6^2 appended:", squares)

# print the size of the list
# your code here
print("length of squares:", len(squares))

# Create and print a list named oddItems with different types of things, in this case [apple, pear, -42]
# Note that apple is text, so that needs to be entered differently than a number. 
oddItems = ["apple", "pear", -42]
# print this list
# your code here
print("full list of oddItems:", oddItems)

# """"""""""""""""""""
# A0-Part-2: slicing.
# """"""""""""""""""""

# Using slicing, print the second, third, and fourth items in the squares list
# your code here
print("second, third, and fourth items of the squares list:", squares[1:4])

# using slicing, print every second element from the list, staring from the first item
# your code here
print("every second element of the squares list:", squares[::2])

# using slicing with a negative index, print the next-to-last item in the squares list
# your code here
print("the next-to-last item in the squares list (should be 25):", squares[-2:])

# """""""""""""""""""""""
# A0-Part-3: matplotlib
# """""""""""""""""""""""
# print a graph of the squares list
# plt.plot(# your code here)
# plt.show()

# this code is provided as an example. Make sure it works with your prior code
integers = [1, 2, 3, 4, 5, 6]
plt.scatter(integers, squares, marker='o', color='red')
plt.title("Squares of some integers")
plt.xlabel("integers")
plt.ylabel("squares")
plt.show()

fig, ax = plt.subplots()
ax.stem(integers, squares, basefmt='C0', markerfmt='o')
# https://stackoverflow.com/questions/40894278/vertical-lines-to-points-in-scatter-plot 
plt.show()

x = np.arange(1,13)
y = [15,14,15,18,21,25,27,26,24,20,18,16]

lines = []
for i in range(len(x)):
    pair=[(x[i],0), (x[i], y[i])]
    lines.append(pair)

linecoll = matcoll.LineCollection(lines)
fig, ax = plt.subplots()
ax.add_collection(linecoll)

plt.scatter(x,y)

plt.xticks(x)
plt.ylim(0,30)

plt.show()

# """""""""""""""""""""""""
# A0-Part-4: numpy arrays
# to be added later
# """""""""""""""""""""""""

# arange

# slicing of a numpy array. Does it differ from slicing of a list? 

# different ways to print a numpy array



