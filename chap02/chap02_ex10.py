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


# In[5]:


ft = interp1d(n,xn,kind = "cubic")
tn = np.linspace(-25,25,1000)


# In[9]:


plt.rcParams["figure.figsize"] = (16,9)
plt.rcParams["lines.linewidth"] = 1


# In[10]:


plt.subplot(2,1,1); plt.stem(n,xn,"blue"); plt.ylabel("x(n)"); plt.grid()
plt.title("Signal reconstruction using first-order interpolation")
plt.subplot(2,1,2); plt.plot(tn,ft(tn),"red"); plt.grid()
plt.xlabel("tn"); plt.ylabel("xa(t)")
plt.stem(n,xn,"blue",".") # 덧그리기


# In[ ]:




