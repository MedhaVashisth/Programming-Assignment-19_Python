#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to find the first
# repeated character in a string
def firstRepeatedChar(str):

	h = {} # Create empty hash

	# Traverse each characters in string
	# in lower case order
	for ch in str:

		# If character is already present
		# in hash, return char
		if ch in h:
			return ch;

		# Add ch to hash
		else:
			h[ch] = 0

	return ''


# Driver code
print(firstRepeatedChar("geeksforgeeks"))


# In[3]:


def reverse(arg):
	if isinstance(arg, bool):
		return not arg
	else:
		return('boolean expected')

def reverse(arg=None):
	return not arg if type(arg) == bool else "boolean expected"

print(reverse(True)) # False
print(reverse(False)) # True
print(reverse(0)) # "boolean expected"
print(reverse(None)) # "boolean expected"


# In[8]:


"""
Folding paper in half 50 times is 3/4 of the distance from earth to sun
From:
http://www.quora.com/What-are-some-of-the-most-mind-blowing-facts#answer_526501
Thickness of a sheet of paper: 0.1 mm (~0.004 inches)
"""


def fold(num_folds=50, thickness=0.1):
    """Simulate folding a sheet of paper in half.
    ``num_folds`` is the number of times we'll fold the paper in half.
    ``thickness`` is the the thickness of a sheet of paper (in millimeters).
    """

    for i in range(1, num_folds + 1):
        thickness = thickness * 2

        if thickness >= 1000000:
        # convert to kilometers
        t = thickness / 1000000.0
        units = 'km'
    elif thickness >= 1000:
        # convert to meters
        t = thickness / 1000.0
        units = 'm'
    elif thickness >= 10:
        # convert to centimeters
        t = thickness / 10.0
        units = 'cm'
    else:
        # keep in millimeters
        t = thickness
        units = 'mm'

        fmt_string = '{n} folds, thickness = {thickness:G} {units}'
        print(fmt_string.format(n=i, thickness=t, units=units))


if __name__ == "__main__":
    n = input("\n\nHow many folds? ")
    fold(n)


# In[9]:


# Python3 code to demonstrate working of
# Uppercase Indices
# Using list comprehension + range() + isupper()

# initializing string
test_str = 'GeeKsFoRGEEks'

# printing original string
print("The original string is : " + str(test_str))

# Uppercase check using isupper()
res = [idx for idx in range(len(test_str)) if test_str[idx].isupper()]

# printing result
print("Uppercase elements indices : " + str(res))


# In[10]:


# Python program to print Even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 == 0:
		print(num, end=" ")


# In[ ]:




