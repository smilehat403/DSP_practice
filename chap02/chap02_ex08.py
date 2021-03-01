#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pylab as plt
from scipy.interpolate import *


# In[2]:


fs = 5000; Ts = 0.0002
n = np.arange(-25,26)
xn = np.exp(-1000*abs(n*Ts))
N = len(n)


# In[13]:


# 영차보간 적용
ft = interp1d(n,xn,kind="previous")
# 보간할 미세구간 설정
tn = np.linspace(-25,25,1000) # 1000번 잘라서 보간한다는 뜻


# In[14]:


plt.rcParams["figure.figsize"] = (16,9)
plt.rcParams["lines.linewidth"] = 1


# In[15]:


plt.subplot(2,1,1); plt.stem(n,xn,"blue"); plt.ylabel("x(n)"); plt.grid()
plt.title("Signal reconstruction using zero-order interpolation")
plt.subplot(2,1,2); plt.plot(tn,ft(tn),"red"); plt.grid()
plt.xlabel("tn"); plt.ylabel("xa(t)")
plt.stem(n,xn,"blue",".") # 덧그리기


# In[ ]:




