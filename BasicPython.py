#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Variable and Operators 1
x=3
y=2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x**y)


# In[21]:


# Variable and Operators 2
temp_c = float(input('Nhập nhiệt độ theo độ C: '))
temp_f = ((9/5) * temp_c) + 32
print('Nhiệt độ F là: ', temp_f)


# In[22]:


# Variable and Operators 3
a = 5
b = 8
print(a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)


# In[23]:


# Function 1
import math
x = 2
print(math.exp(x))


# In[24]:


# Function 2
import random
print(random.random())
print(random.random())
print(random.random())
print(random.random())


# In[25]:


# Selection constructs
def ReLU(x):
    result = 0
    if x>0:
        result = x
    return result

value1 = ReLU(x=5)
value2 = ReLU(x=-2)

print(value1)
print(value2)


# In[26]:


# Loop constructs
# For Loop
for i in range(10):
    if i==5:
        continue
        
    print('Giá trị i là', i)


# In[27]:


# Loop constructs
# While Loop
import random

while True:
    num = random.randint(0,10)
    print('Số sinh ra có giá trị là', num)
    if num==5:
        break;
print('Đã thoát khỏi vòng lặp While')


# In[28]:


# Loop constructs
# For Loop: PI Estimation
import random
import math

N = 100000
N_T = 0

for i in range(N):
    x = random.random()*2 - 1
    y = random.random()*2 - 1
    
    x2 = x**2
    y2 = y**2
    
    if math.sqrt(x2 + y2) <= 1.0:
        N_T = N_T + 1
        
pi = (N_T/N)*4
print(pi)


# In[29]:


# Loop constructs
# Euler's number
def factorial(n):
    result = 1
    for i in range(2,n+1):
        result = result*i
        
    return result

def estimate_e(n):
    result = 1
    for i in range(1,n+1):
        result = result + 1/factorial(i)
        
    return result

print(estimate_e(10))


# In[52]:


# Loop constructs
# Simulation of coin tossing
import random

total_flips = 0
num_tails = 0
num_heads = 0

for _ in range(1000):
    n = random.random()
    if n < 0.5:
        num_tails = num_tails + 1
    else:
        num_heads = num_heads + 1
        
    total_flips = total_flips + 1
    
print('Xác xuất tung được mặt sau là ',str(num_tails/total_flips*100)+'%')
print('Xác xuất tung được mặt trước là ',str(num_heads/total_flips*100)+'%')


# In[ ]:




