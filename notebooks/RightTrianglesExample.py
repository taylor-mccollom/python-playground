#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# You have a warehouse of triangles
# You have a database for this warehouse which contains the dimmensions of each triangle
# the data comes to you in the form of a list of lists where each inner list contains the 3 sides to a triangle

# Write a program which loops over each triangle and determines whether or not it is a right triangle
# The output should be a new list which only contains right triangles


# In[ ]:


"""
a**2 + b**2 = c**2

c = (a**2 + b**2)**0.5

   |\
 a | \  c
   |  \
   |___\
     b
"""


# In[1]:


# Here is the output from your database of triangles

triangles = [
    [3, 4, 5],
    [5, 5, 50],
    [5, 12, 13],
    [1, 3, 7],
    [9, 14, 90],
    [3, 8, 10],
    [2, 7, 9],
    [6, 8, 10]
]


# In[14]:


# STEP1
# write a function which determines whether or not a triangle is a right triangle based on the dimmensions

# function is it right needs to find max of list and assign to c
# create variables for two other sides by indexing at 0 and 1
# check if a**2+b**2==c**2, and if true return answer


def right_checker(triangle):
    c = max(triangle)
    b = triangle[1]
    a = triangle[0]
    is_right = (a**2 + b**2) == c**2
    return is_right


# In[15]:


# STEP2
# Create a new empty list where you will store the dimmensions of all the right triangles
tri_check = []


# In[23]:


# STEP3
# Loop over each triangle, determine if its a right triangle using your function, and append to the new list if it is
for triangle in triangles:
    is_right = right_checker(triangle)
    print(f'Checking if {triangle} is right')
    if is_right:
        print(triangle, "is a right triangle!")
        tri_check.append(triangle)
    else:
        print(f'{triangle} is not a right triangle.')


# In[ ]:





# In[ ]:




