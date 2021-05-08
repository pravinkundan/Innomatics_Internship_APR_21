#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1
def swap_case(s):
    return s.swapcase()


# In[2]:


# Question 2
def split_and_join(line):
    # write your code here
    x = line.split()
    x = "-".join(x)
    return x


# In[3]:


# Question 3
def print_full_name(first, last):
    # Write your code here
    print("Hello {} {}! You just delved into python.".format(first,last))


# In[4]:


# Question 4
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]


# In[5]:


# Question 5
def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)-len(sub_string)+1):
        l = i
        for j in range(0, len(sub_string)):
            if string[l] == sub_string[j]:
                l +=1
                if j == len(sub_string)-1:
                    count = count + 1
                else:
                    continue
            else:
                break
            
    return count


# In[6]:


# Question 6
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))


# In[7]:


# Question 7
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# In[8]:


# Question 8
def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))


# In[10]:


# Question 9
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


# In[11]:


# Question 10
def print_formatted(number):
    # your code goes here
    l = len(bin(n)) - 2

    for i in range(1, n + 1):
        f = ""
        for c in "doXb":
            if f:
                f += " "
            f += "{:>" + str(l) + c + "}"
        print(f.format(i, i, i, i))


# In[12]:


# Question 11
def print_rangoli(size):
    # your code goes here
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(n)]
    items = list(range(n))
    items = items[:-1]+items[::-1]
    for i in items:
        temp = data[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3, "-"))


# In[13]:


# Question 12
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s


# In[14]:


# Question 13
def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    Stuart_score, Kevin_score = 0, 0
    length = len(string)
    for start_idx in range(length):
        score = length - start_idx
        if string[start_idx] in vowels:
            Kevin_score += score
        else:
            Stuart_score += score
    if Stuart_score == Kevin_score:
        print('Draw')
    if Stuart_score > Kevin_score:
        print('Stuart {}'.format(Stuart_score))
    if Stuart_score < Kevin_score:
        print('Kevin {}'.format(Kevin_score))


# In[15]:


# Question 14
def merge_the_tools(string, k):
    # your code goes here
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))


# In[ ]:




