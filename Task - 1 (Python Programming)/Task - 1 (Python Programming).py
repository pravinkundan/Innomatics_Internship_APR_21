#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1
print("Hello, World!")


# In[2]:


#Question 2
if __name__ == '__main__':
    n = int(input().strip())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n in range(2,6):
    print("Not Weird")
elif n % 2 == 0 and n in range(6,21):
    print("Weird")
else :
    print("Not Weird")


# In[5]:


#Question 3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# In[6]:


#Question 4
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


# In[7]:


#Question 5
if __name__ == '__main__':
    n = int(input())
    for i in range (n):
        print(i*i)


# In[10]:


#Question 6
def is_leap(year):
    leap = False
    
    # Write your logic here
    return year % 4 ==0 and (year % 400 ==0 or year % 100 !=0)

year = int(input())
print(is_leap(year))


# In[9]:


#Question 7
if __name__ == '__main__':
    n = int(input())
    for i in range (1,n+1):
        print(i,end="")


# In[ ]:





# In[ ]:





# In[ ]:




