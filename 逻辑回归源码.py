'''
逻辑回归：目的：找到决策边界,1-先求出theta，得到拟合函数
'''
import time
import numpy as np
import matplotlib.pyplot as plt

data = [(34.62,78.02,0),
        (30.28,43.89,0),
        (35.84,72.90,0),
        (60.18,86.30,1),
        (79.03,75.34,1) ]

i = 0
t = []
theta0 = []
theta1 = []
theta2 = []

alpha = 0.000001
variance = 0.00001

theta0_guess = 1.
theta0_last  = 100.
theta1_guess = 1.
theta1_last  = 100.
theta2_guess = 1.
theta2_last  = 100.

# def g(theta,x):
#     return -theta * x # theta 权重向量

def hyper(theta0,theta1,theta2,x1,x2):
    #z = g(theta,x)
    return 1/(1+np.exp(- theta2 * x2 - theta1 * x1 - theta0))

#def Jtheta():
while(abs(theta0_guess - theta0_last) > variance or
       abs(theta1_guess - theta1_last) > variance or
       abs(theta2_guess - theta2_last) > variance ):
    i+=1
    theta0_last = theta0_guess
    theta1_last = theta1_guess
    theta2_last = theta2_guess
    
    theta0_guess = theta0_guess - alpha * sum([(hyper(theta0_guess,theta1_guess,theta2_guess,point[0],point[1])-point[2])  for point in data])  #Xi损失函数对theta求导
    theta1_guess = theta1_guess - alpha * sum([(hyper(theta0_guess,theta1_guess,theta2_guess,point[0],point[1])-point[2]) * point[0] for point in data])
    theta2_guess = theta2_guess - alpha * sum([(hyper(theta0_guess,theta1_guess,theta2_guess,point[0],point[1])-point[2]) * point[1] for point in data])
    
    theta0.append(theta0_guess)
    theta1.append(theta1_guess)
    theta2.append(theta2_guess)
    t.append(i)

print(theta0_guess,theta1_guess,theta2_guess)

x = []
y = []
for i in range(5):
    x.append(data[i][0])
    y.append(data[i][1])
plt.scatter(x, y, s=50, c='r', marker='x')

plt.figure()
plt.subplot(311)
plt.plot(t,theta0)
plt.subplot(312)
plt.plot(t,theta1)
plt.subplot(313)
plt.plot(t,theta2)
plt.tight_layout()
