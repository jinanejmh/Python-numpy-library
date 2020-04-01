# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:29:13 2020

@author: Jinane Jmh
"""


import numpy as np

# ndim : find the dimension of the array
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)

#itemsize : calculate the byte size of each element
b = np.array([(1,2,3)])
print(b.itemsize)

#dtype : the data type of the elements that are stored in an array
c = np.array([(1,2,3)])
print(c.dtype)
#size and shape functionality return the size and shape
print(c.size)
print(c.shape)

#reshape : change the number of rows and columns which gives a new view to an object
d = np.array([(8,9,10),(11,12,13)])
print(a)
d=d.reshape(3,2)
print(d)

#Slicing :extracting particular set of elements from an array
#in this case : when I have written 0:2,
# this does not include the second index of the third row of an array. 
#Therefore, only 9 and 11 gets printed else you will get all the elements i.e [9 11 13].
a=np.array([(8,9),(10,11),(12,13)])
print(a[0:2,1])

#linespace: returns evenly spaced numbers over a specified interval
e=np.linspace(1,3,10)
print(e)

#min , max , sum : find the minimum, maximum as well the sum of the numpy array
f= np.array([1,2,3])
print(f.min())
print(f.max())
print(f.sum())

#sqrt , std : find the square root, standard deviation of the array
g=np.array([(1,2,3),(3,4,5,)])
print(np.sqrt(g))
print(np.std(g))

#addition ,substraction , multiplication and division
x= np.array([(1,2,3),(3,4,5)])
y= np.array([(1,2,3),(3,4,5)])
print(x+y)
print(x-y)
print(x*y)
print(x/y)

#vertical stacking and horizontal stacking
#to concatenate two arrays and not just add them, you can perform it using two ways 
x= np.array([(1,2,3),(3,4,5)])
y= np.array([(1,2,3),(3,4,5)])
print(np.vstack((x,y)))
print(np.hstack((x,y)))

#ravel : convert one numpy array into a single column 
x= np.array([(1,2,3),(3,4,5)])
print(x.ravel())
