#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# 샘플링주파수 100HZ, 0.01초 간격으로 300개 샘플
fs=100; dt=1/fs; N=300

# 시간축은 0.01초*300샘플 = 3초
t=np.arange(0,N)*dt
x1t = 1.0*np.sin(2*np.pi*1*t)
x2t = 1/3*np.sin(2*np.pi*3*t)
x19t = 1/19*np.sin(2*np.pi*19*t)

sum = 0

for i in range(1,20,2):
    sum += (1/i)*np.sin(2*np.pi*i*t)

xt = sum


# In[3]:


# 주파수 간격
df = fs/N
f = np.arange(0,N)*df
# 주파수별 크기 계산
Xf = np.fft.fft(xt)


# In[5]:


plt.subplot(6,1,1); plt.plot(t,xt,"b"); plt.ylim(-1,1); plt.grid()
plt.ylabel("x(t)")
plt.title("A periodic signal x(t)=x1(t)+x2(t)+...+x19(t)")

plt.subplot(6,1,2); plt.plot(t,x1t,"b"); plt.ylim(-1,1); plt.grid()
plt.ylabel("x1(t)")

plt.subplot(6,1,3); plt.plot(t,x2t,"b"); plt.ylim(-1,1); plt.grid()
plt.ylabel("x2(t)")

plt.subplot(6,1,5); plt.plot(t,x19t,"b"); plt.ylim(-1,1); plt.grid()
plt.ylabel("x19(t)")

plt.subplot(6,1,6); plt.plot(f[0:int(N/2+1)],np.abs(Xf[0:int(N/2+1)]),"b")
plt.xlabel("frequency(Hz)"); plt.ylabel("Spectrum X(f)"); plt.grid()

