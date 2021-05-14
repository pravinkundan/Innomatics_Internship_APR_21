#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1
def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr[::-1],float)


# In[2]:


# Question 2
import numpy
my_array = numpy.array(input().split(),int)
print(my_array.reshape(3,3))


# In[3]:


# Question 3
import numpy
n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())


# In[4]:


# Question 4
import numpy
n,m,p = map(int,input().split())
arr1 = numpy.array([input().split() for _ in range(n)],int)
arr2 = numpy.array([input().split() for _ in range(m)],int)
print(numpy.concatenate((arr1,arr2),axis = 0))


# In[5]:


# Question 5
import numpy
array = tuple(map(int,input().split()))
print(numpy.zeros(array, dtype = numpy.int))
print(numpy.ones(array, dtype = numpy.int))


# In[6]:


# Question 6
import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))


# In[7]:


# Question 7
import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')


# In[8]:


# Question 8
import numpy
numpy.set_printoptions(sign = ' ')
arr1 = numpy.array(input().split(),float)
print(numpy.floor(arr1))
print(numpy.ceil(arr1))
print(numpy.rint(arr1))


# In[9]:


# Question 9
import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))


# In[10]:


# Question 10
import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(A, axis=1)))


# In[11]:


# Question 11
import numpy
N,M = map(int, input().split(" "))
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.mean(A, axis = 1))
print(numpy.var(A, axis = 0))
print(round(numpy.std(A, axis = None),11))


# In[12]:


# Question 12
import numpy
n=int(input())
a = numpy.array([input().split() for _ in range(n)],int)
b = numpy.array([input().split() for _ in range(n)],int)
m = numpy.dot(a,b)
print (m)


# In[13]:


# Question 13
import numpy
m = numpy.array(input().split(), int)
n = numpy.array(input().split(), int)
print((numpy.inner(m,n)), (numpy.outer(m,n)), sep = '\n')


# In[14]:


# Question 14
import numpy
n = list(map(float,input().split()));
m = input();
print(numpy.polyval(n,int(m)));


# In[15]:


# Question 15
import numpy
n=int(input())
a=numpy.array([input().split() for _ in range(n)],float)
numpy.set_printoptions(legacy='1.13') #important
print(numpy.linalg.det(a))


# In[ ]:




