#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


# 샘플링 주파수와 주기
fs=5000; Ts = 0.0002
# 인덱스 어레이
n = np.arange(-25,26)
# 샘플 신호
xn = np.exp(-1000*np.abs(n*Ts))
N = len(n)

# 시간 간격
dt = 0.00005
# sinc함수 시간축 >> 임펄스 신호는 [-fs/2, fs/2]의 대역폭을 가진 ideal LPF를 통과해야 한다.
#                 >> sinc()함수는 interpolating function이다
t = np.arange(-0.005, 0.005,dt)
# sinc함수의 시간축 길이
Nt = len(t)


# In[24]:


# 복원결과 출력배열
sinc_out = np.zeros(Nt)
for i in range(Nt):
    sum = 0 
    for j in range(N):  # n에서의 결과값과 싱크함수를 곱한다음 합을 구한다.
        sum += xn[j]*np.sinc(fs*(i*dt-j*Ts))
    sinc_out[i] = sum

print(sinc_out)


# In[25]:


plt.rcParams["figure.figsize"] = (16,9)
plt.rcParams['lines.linewidth'] = 1

plt.subplot(2,1,1); plt.stem(n,xn,"b"); plt.ylabel("x(n)"); plt.grid()
plt.title("x(n), Reconstructed signal using sinc function")
plt.subplot(2,1,2); plt.plot(t,sinc_out,"red")
plt.xlabel("time in msec"); plt.ylabel("x(t)"); plt.grid()


# In[ ]:




