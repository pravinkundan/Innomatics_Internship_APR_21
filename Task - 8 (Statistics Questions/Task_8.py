#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1
import math

def bi_dist(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

b, p, n = 0, 1.09/2.09, 6
for i in range(3,7):
    b += bi_dist(i, n, p)   
print("%.3f" %b)


# In[2]:


# Question 2
def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

p, n = list(map(int, input().split(" ")))
print(round(sum([b(i, n, p/100) for i in range(3)]), 3))
print(round(sum([b(i, n, p/100) for i in range(2, n+1)]), 3))


# In[3]:


# Question 3
import math
mean, std = 20, 2
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# Less than 19.5
print('{:.3f}'.format(cdf(19.5)))
# Between 20 and 22
print('{:.3f}'.format(cdf(22) - cdf(20)))


# In[4]:


# Question 4
import math
mean, std = 70, 10
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

print(round((1-cdf(80))*100,2))
print(round((1-cdf(60))*100,2))
print(round((cdf(60))*100,2))


# In[5]:


# Question 5
import math

def NormalPDF(stddev, mean, x):
    return 0.5 * (1 + math.erf((x - mean) / (stddev * (2 ** 0.5))))

max_weight = float(input().strip())
no_of_boxes = float(input().strip())
mean = float(input().strip())
stddev = float(input().strip())

print(round(NormalPDF(stddev * (no_of_boxes ** 0.5), mean * no_of_boxes, max_weight), 4))


# In[6]:


# Question 6
import math

def NormalPDF(stddev, mean, x):
    return 0.5 * (1 + math.erf((x - mean) / (stddev * (2 ** 0.5))))

max_weight = float(input().strip())
no_of_boxes = float(input().strip())
mean = float(input().strip())
stddev = float(input().strip())

print(round(NormalPDF(stddev * (no_of_boxes ** 0.5), mean * no_of_boxes, max_weight), 4))


# In[7]:


# Question 7
n = float(input().strip())
mean = float(input().strip())
stddev = float(input().strip())
percent_ci = float(input().strip())
value_ci = float(input().strip())

print(round(mean - (value_ci * (stddev / (n ** 0.5))), 2))
print(round(mean + (value_ci * (stddev / (n ** 0.5))), 2))


# In[8]:


# Question 8
n = int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))

mu_x = sum(X) / n
mu_y = sum(Y) / n

stdv_x = (sum([(i - mu_x)**2 for i in X]) / n)**0.5
stdv_y = (sum([(i - mu_y)**2 for i in Y]) / n)**0.5


covariance = sum([(X[i] - mu_x) * (Y[i] -mu_y) for i in range(n)])

correlation_coefficient = covariance / (n * stdv_x * stdv_y)


# In[9]:


# Question 9
import statistics as st

n = 5
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
meanX = st.mean(x)
meanY = st.mean(y)
x_s = sum([x[i] ** 2 for i in range(5)])
xy = sum([x[i]*y[i] for i in range(5)])

b = (n * xy - sum(x) * sum(y)) / (n * x_s - (sum(x) ** 2))
a = meanY - b * meanX

print (round(a + 80 * b, 3))


# In[10]:


# Question 10
import numpy as np

def solve(y, x, x_pred):
  # x transpose
  x_dash  = x.T
  # product of x_dash and x
  X       = x_dash.dot(x)
  # inverse of X
  X_inv   = np.linalg.inv(X)
  # producet of X_inv and x_dash
  X_final = X_inv.dot(x_dash)
  # product of X_final and y i.e B
  B       = X_final.dot(y)
  # calculate the y_pred
  y_pred  = x_pred.dot(B)
  return y_pred

def main():
  m, n = map(int, input().strip().split())
  y = []; x = []; x_pred = []
  for _ in range(n):
    *features, y_val = map(float, input().strip().split())
    x.append([1] + features)
    y.append(y_val)

  for _ in range(int(input())):
    features = list(map(float, input().strip().split()))
    x_pred.append([1] + features)

  y = np.array(y)
  x = np.array(x)
  x_pred = np.array(x_pred)
  answer = solve(y, x, x_pred)
  
  for num in answer:
    print(round(num, 2))

if __name__ == "__main__":
  main()


# In[ ]:




