# sample code modified by jhun baclaan
# d.o.c. (date of creation): jan. 15, 2026

# Some Foundational Python: lists, slicing, matplotlib, numpy arrays

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import collections as matcoll

# """"""""""""""""""""
# A0-Part-1: lists
# """"""""""""""""""""
print("---------- A0-Part-1: lists ----------")
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
print("---------- A0-Part-2: slicing ----------")
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
print("---------- A0-Part-3: matplotlib ----------")
# print a graph of the squares list
plt.plot(squares)
plt.show()

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
# """""""""""""""""""""""""
print("---------- A0-Part-4: numpy arrays ----------")

# some examples - you don't need to code: 
# create a NumPy array using the numpy array() function and a list
arr = np.array([1, 2, 3, 4, 5])
print(arr)

myList = [1, 2, 3, 4, 5]
print(myList)
arr = np.array(myList)
print(arr)               # note how the list is printed differently than the array

print(myList[1])
print(arr[1])

# numpy.arange
print(np.arange(5))
print(np.arange(5 , 10))  # integers from 5 to 9

# some examples - you do need to code:

# using numpy.arange create a NumPy array with integers from 5 to 10 inclusive 
# your code here
print("numpy array with integers 5 to 10 inclusive: ", np.arange(5,11))

# using numpy arange, create then print a NumPy array named sequence
# with floating-point numbers from 0 to 1.0, with a 0.1 interval
# your code here
sequences = np.arange(0.0, 1.1, 0.1)
print("numpy array \"sequences\" (array from 0 to 1.0 with intervals of 0.1): ", sequences)

# print the number of dimensions of sequences using the ndim attribute
# print the datatype of sequences using the dtype attribute
# print the number of elements in sequences using the size attribute
# your code here
print("number of dimensions in sequences: ", sequences.ndim)
print("datatype of sequences: ", sequences.dtype)
print("amount of elements in sequences: ", np.size(sequences))

# using numpy arange, create then print a numpy array with integers from 10 to 1 inclusive,
# using a negative step value to create the array in reverse order. 
# your code here
negativeInts = np.arange(10, 0, -1)
print("numpy array \"negativeInts\" that goes from 10 to 1 inclusive, in descending order: ", negativeInts)

# linspace
# using numpy linspace, create and print a numpy array with 20 numbers from 0 to 1, inclusive
# your code here
twentyInclusive = np.linspace(0,1, num=20)
print("numpy array created with linspace: ", twentyInclusive)

# """""""""""""""""""""""
# A0-Part-5: tuples
# """""""""""""""""""""""
print("---------- A0-Part-5 tuples ----------")

# create a tuple named nums with (0, 1, 2, 3, 4, 5), and print it
# your code here
nums = (0, 1, 2, 3, 4, 5)
print("all elements of a tuple named \"nums\": ", nums)

# print the third item in nums using indexing
# your code here
print("third item in nums: ", nums[2])

# print the last two items in nums using negative slicing
# your code here
print("last two items in nums: ", nums[-2:])
# print the odd numbers in nums using slicing
# your code here
print("odd numbers in nums: ", nums[1::2])
# using the tuple constructor create a tuple called fives containing 10, 15, 20, 25, and
# print the even numbers in it using slicing
# your code here
fives = tuple(range(10,30,5))
print("even numbers in a a tuple named \"fives\": ", fives[::2])

# print the type of fives
# your code here
print("data type of fives: ", type(fives))
