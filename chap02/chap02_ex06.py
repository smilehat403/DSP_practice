#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[6]:


# 주파수 축 설정
w = np.arange(-2*np.pi, 2*np.pi, 0.1)
# 전체 주파수축 길이
N = len(w)
# CTFT 결과 값(y)를 저장하기 위한 행렬
Xw = np.zeros(N)
T = 1
# print(w,len(w))
# print(Xw,len(Xw))


# In[19]:


for i in range(-int(N/2),int(N/2)):
    if i==0:
        Xw[i+int(N/2)] = 1  # int(N/2)만큼 평행이동
    else:
        Xw[i+int(N/2)] = np.sin(i*T/2)/(i/2)


# In[22]:


plt.rcParams["figure.figsize"] = (14,4)
plt.rcParams['lines.linewidth'] = 1
# plt.rcParams['lines.color'] = 'r'
plt.rcParams['axes.grid'] = True 
# plt.text(3.5, 3.0, '평균:2.5')

plt.plot(w,Xw,"b"); plt.stem(w,Xw,"b")
plt.xlabel("w, freq in radians"); plt.ylabel("X(w)")
plt.title("CTFT, of a non-periodic signal")


# In[ ]:




