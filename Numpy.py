#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Tạo ndarray từ list
import numpy as np

l = list(range(1,4))
data = np.array(l)

print(data)
print(data[0])
print(data[1])


# In[4]:


# Tạo ndarray từ list
import numpy as np

list1D = [1,2,3]
data = np.array(list1D)

print(data)
print(data.shape)


# In[12]:


# Tạo ndarray từ list
import numpy as np

list3D = [[[1,6],[2,2],[3,4]],
         [[4,7],[5,2],[6,9]],
         [[7,7],[8,2],[9,5]]]

data = np.array(list3D)

print(data.shape)


# In[15]:


# Tạo ndarray từ list
import numpy as np

data1 = np.array([1,2,3])
print(data1.dtype)

data2 = np.array([1.,2.,3.])
print(data2.dtype)

data3 = np.array([1,2,3], dtype=np.int64)
print(data3.dtype)


# In[16]:


# Thay đổi giá trị phần tử
import numpy as np

l = list(range(1,4))
data = np.array(l)

print(data)

data[0] = 8
print(data)


# In[17]:


# Tạo 1 Numpy array với tất cả các phần tử là 0
import numpy as np

arr = np.zeros((2,3))
print(arr)


# In[18]:


# Tạo 1 Numpy array với tất cả các phần tử là 1
import numpy as np

arr = np.ones((2,3))
print(arr)


# In[19]:


# Tạo 1 Numpy array với tất cả các phần tử là hằng số fill_value
import numpy as np

arr = np.full((2,3),9)
print(arr)


# In[20]:


# Tạo 1 Numpy array
import numpy as np

arr1 = np.arange(5)
print(arr1)

arr2 = np.arange(0,5,2)
print(arr2)


# In[21]:


# Tạo 1 Numpy array với đường chéo là số 1, số 0 điền vào ô còn lại
import numpy as np

arr = np.eye(3)
print(arr)


# In[22]:


# Tạo 1 Numpy array với giá trị ngẫu nhiên
import numpy as np

arr = np.random.random((2,3))
print(arr)


# In[23]:


# Where function
import numpy as np

arr = np.arange(5)
print(arr)

condition = arr < 3
out = np.where(condition, arr, arr * 2)

print(condition)
print(out)


# In[24]:


# Flatten function
import numpy as np

arr = np.array([[2,3], [3,4]])
out = arr.flatten()

print(arr)
print(out)


# In[25]:


# Reshape function
import numpy as np

l = [[1,2,3],
     [4,5,6]]

data = np.array(l)
print(data)
print(data.shape)

data_rs = np.reshape(data, (3,2))
print(data_rs)
print(data_rs.shape)


# In[26]:


# Slicing
import numpy as np

a_arr = np.array([[1,2,3],
                  [5,6,7]])

b_arr = a_arr[:, 1:3]

print(a_arr)
print(b_arr)


# In[27]:


# Slicing - Mutable
import numpy as np

a_arr = np.array([[1,2,3],
                  [5,6,7]])
print(a_arr)

b_arr = a_arr[:, 1:3]
print(b_arr)

print(a_arr[0,1])
b_arr[0,0] = 99
print(a_arr[0,1])


# In[28]:


# Get a row
import numpy as np

arr = np.array([[1,2,3],
                [5,6,7],
                [9,10,11]])

row_m1 = arr[1, :]

row_m2 = arr[1:2, :]

print(row_m1, row_m1.shape)
print(row_m2, row_m2.shape)


# In[29]:


# Get a column
import numpy as np

arr = np.array([[1,2,3],
                [5,6,7],
                [9,10,11]])

col_m1 = arr[:, 1]

col_m2 = arr[:, 1:2]

print(col_m1, col_m1.shape)
print(col_m2, col_m2.shape)


# In[30]:


# Using Lists as indices
import numpy as np

arr = np.array([[1,2],
                [3,4],
                [5,6]])

out1 = arr[[0,1,2],[0,1,0]]
print('out1:\n', out1)

out2 = arr [[0,0],[1,1]]
print('out2:\n', out2)


# In[31]:


# Boolean indices
import numpy as np

arr = np.array([[1,2],
                [3,4],
                [5,6]])

print(arr)

bool_idx = (arr >2)
print(bool_idx)


# In[32]:


# Addition
import numpy as np

x = np.array([1,2,3,4])
y = np.array([5,6,7,8])

print('data x \n', x)
print('data y \n', y)

print('method 1 \n', x+y)
print('method 2 \n', np.add(x,y))


# In[34]:


# Subtraction
import numpy as np

x = np.array([5,6,7,8])
y = np.array([1,2,3,4])

print('data x \n', x)
print('data y \n', y)

print('method 1 \n', x-y)
print('method 2 \n', np.subtract(x,y))


# In[35]:


# Multiplication
import numpy as np

x = np.array([1,2,3,4])
y = np.array([5,6,7,8])

print('data x \n', x)
print('data y \n', y)

print('method 1 \n', x*y)
print('method 2 \n', np.multiply(x,y))


# In[36]:


# Division
import numpy as np

x = np.array([5,6,7,8])
y = np.array([1,2,3,4])

print('data x \n', x)
print('data y \n', y)

print('method 1 \n', x/y)
print('method 2 \n', x//y)
print('method 3 \n', np.divide(x,y))


# In[37]:


# Căn bậc 2 từng phần tử trong data
import numpy as np

data = np.array([1,2,3,4])
print('data \n', data)
print('sqrt \n', np.sqrt(data))


# In[38]:


# Tính inner product giữa v và w
import numpy as np

v = np.array([1,2])
w = np.array([2,3])

print('method 1 \n', v.dot(w))
print('method 2 \n', np.dot(v,w))


# In[39]:


# Phép nhân giữa ma trận và vector
import numpy as np
v = np.array([[1,2],
              [3,4]])
w = np.array([1,2])

print('matrix X \n', v)
print('vector v \n', w)

print('method 1: X.dot(v) \n', v.dot(w))
print('method 1: v.dot(X) \n', w.dot(v))


# In[40]:


# Phép nhân giữa 2 ma trận
import numpy as np

X = np.array([[1,2],
              [3,4]])
Y = np.array([[2,3],
              [2,1]])

print('method 1 \n', X.dot(Y))
print('method 2 \n', Y.dot(X))


# In[41]:


# Chuyển vị
import numpy as np

X = np.array([[1,2],
              [3,4]])

print(X)
print(X.T)


# In[42]:


# Tính tổng
import numpy as np

X = np.array([[1,2],
              [3,4]])

# Tổng các pt của mảng
print(np.sum(X))

# Tính tổng theo từng cột
print(np.sum(X, axis = 0))

#Tính tổng theo từng dòng
print(np.sum(X, axis=1))


# In[43]:


# Max and min
import numpy as np

data = np.array([1,2,3])

print(data.max())
print(data.min())


# In[44]:


# Broadcasting
import numpy as np

data = np.array([1,2,3])
factor = 2

result_multiplication = data*factor
result_minus = data - factor

print(data)
print(result_multiplication)
print(result_minus)


# In[45]:


# Matrix and vector
import numpy as np

X = np.array([[1,2,3],
              [4,5,6],
              [7,8,9],
              [10,11,12]])
v = np.array([1,0,1])
Y = X + v
print(Y)

