# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nbXAfncwrsh99XeXl1GDlx4I__GMZyKQ
"""

import numpy as np
import matplotlib.pyplot as plt
n = 17 # data points
p = np.linspace(50, 825, 32)
q = np.array([62, 74.7, 79.7, 82, 93.4, 94, 105, 113.82, 139, 135, 138, 130, 148, 160, 161, 170, 175.25, 182.05, 195, 198, 199, 209.37, 220, 227, 229.9, 239, 243.5, 240.33, 243, 269, 270.8, 285])
# write evenly spaced values including first and last values of given data points
K = [q[0]]
c = 0
for c in range(0,len(q),2):
  K.append(q[c+1])
  T = [p[0]]
  c = 0
  for c in range (0,len(p),2):
    T.append(p[c+1])
#define function
def Spline2(T, K):
  k1 = len(T) - 1
  y = [(K[i//2] if i%2==0 else K[(i)//2]) if i <= 2*k1 else 0 for i in range(1, 3*k1 + 1)]
  M = np.zeros([3*k1, 3*k1])
  print(y)
  for i in range(k1):
    M[2*(i + 1) - 2][3*i] = M[2*(i + 1) - 1][3*i] = 1 
    M[2*(i + 1) - 2][3*i + 1] = T[i] 
    M[2*(i + 1) - 2][3*i + 2] = T[i]**2
    M[2*(i + 1) - 1][3*i + 1] = T[i + 1] 
    M[2*(i + 1) - 1][3*i + 2] = T[i + 1]**2
  for i in range(k1 - 1):
    M[2*k1 + i][3*i + 1] = 1
    M[2*k1 + i][3*i + 4] = -1 
    M[2*k1 + i][3*i + 2] = 2*T[i + 1]
    M[2*k1 + i][3*i + 5] = -2*T[i + 1]
  M[3*k1 - 1][2] = 2
  print("M Matrix\n", M)
  Coef = np.matmul(np.linalg.inv(M),y)
  display([['{:30}'.format(str(round(Coef[3*i],3)) + ' + ' + str(round(Coef[3*i + 1],3)) + 'x + ' + str(round(Coef[3*i + 2],3)) + 'x**2'),
            '{:15}'.format(str(round(T[i],3))+' <=x<= '+str(round(T[i + 1],3)))] for i in range(k1)])
  return np.piecewise(x, [(x >= T[i])&(x <= T[i + 1]) for i in range(k1)],
                         [lambda x, j=i: Coef[3*j] + Coef[3*j + 1]*x + Coef[3*j + 2]*x**2 for i in range(k1)])
x = np.arange(50, 825, .0001)
y = Spline2(T, K)
plt.plot(x, y, label="y2")
plt.plot(T, K, 'k*')
plt.title("Quadratic spline")
plt.xlabel("x"); plt.ylabel("y2")
plt.legend(); plt.grid(); plt.show()
np.interp(51, T, K),np.interp(192.8, T, K)