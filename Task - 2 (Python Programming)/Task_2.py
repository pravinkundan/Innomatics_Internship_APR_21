#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 1
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n])


# In[ ]:


# Question 2
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    print(max([i for i in arr if i < max(arr)]))


# In[ ]:


# Question 3
l = []
second_lowest_names = []
scores = set()

for _ in range(int(input())):
    name = input()
    score = float(input())
    l.append([name, score])
    scores.add(score)
        
second_lowest = sorted(scores)[1]

for name, score in l:
    if score == second_lowest:
        second_lowest_names.append(name)


# In[ ]:


# Question 4
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    print( format(sum(student_marks[query_name])/len(student_marks[query_name]), ".2f") )


# In[ ]:


# Question 5
if __name__ == '__main__':
    N = int(input())
    empty = []
    conv = []

    for i in range(N):
        x = input().split()
        empty.append(x)

    for i in range(len(empty)):
        if empty[i][0] == 'insert':
            x = int(empty[i][1])
            y = int(empty[i][2])
            conv.insert(x,y)
        elif empty[i][0] == 'print':
            print(conv)
        elif empty[i][0] == 'remove':
            conv.remove(int(empty[i][1]))
        elif empty[i][0] == 'append':
            conv.append(int(empty[i][1]))
        elif empty[i][0] == 'sort':
            conv.sort()
        elif empty[i][0] == 'pop':
            conv.pop()
        elif empty[i][0] == 'reverse':
            conv.reverse()


# In[ ]:


# Question 6
n = int(input())
int_list = [int(i) for i in input().split()]
int_tuple = tuple(int_list)
print(hash(int_tuple))


# In[ ]:


# Question 7
def average(array):
    # your code goes here
    s = sum(set(array))
    n = len(set(array))
    return s/n


# In[ ]:


# Question 8
n, m = input().split()
arr = input().split()

A = set(input().split())
B = set(input().split())

print (sum([(i in A) - (i in B) for i in arr]))


# In[ ]:


# Question 9
a,b = [set(input().split()) for _ in range(4)][1::2]
print('\n'.join(sorted(a^b, key=int)))


# In[ ]:


# Question 10
n = set()
[n.add(input()) for _ in range(int(input()))]
print(len(n))


# In[ ]:


# Question 11
n = int(input())
s = set(map(int, input().split()))
operation = int(input())

for x in range(operation):
  oper = input().split()
  if oper[0] == "remove":
    s.remove(int(oper[1]))
  elif oper[0] == "discard":
    s.discard(int(oper[1]))
  else:
    s.pop()
    
print(sum(s))


# In[ ]:


# Question 12
n = int(input())
l = list(input().split())
b = int(input())
k = list(input().split())

s1 = set(l)
s2 = set(k)

print(len(s1.union(s2)))


# In[ ]:


# Question 13
_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.intersection(b)))


# In[ ]:


# Question 14
n1 = int(input())
set_n1 = set(map(int,input().split()))
n2 = int(input())
set_n2 = set(map(int,input().split()))
print(len(set_n1-set_n2))


# In[ ]:


# Question 15
_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.symmetric_difference(b)))


# In[ ]:


# Question 16
if __name__ == '__main__':
    (_, A) = (int(input()),set(map(int, input().split())))
    B = int(input())
    for _ in range(B):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        getattr(A, command)(newSet)

    print (sum(A))


# In[ ]:


# Question 17
k = int(input())
arr = list(map(int, input().split()))

myset = set(arr)

print(((sum(myset)*k)-(sum(arr)))//(k-1))


# In[ ]:


# Question 18
for _ in range(int(input())):
    x = input()
    a = set(input().split())
    y = input()
    b = set(input().split())
    
    print(a.issubset(b))


# In[ ]:


# Question 19
a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))

