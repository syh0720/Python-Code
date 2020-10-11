'''
随机梯度下降法(1)一个特征量
'''
import random
import matplotlib.pyplot as plt

data = [   
 (2104,39990),
 (1600,32990),
 (2400,36900),
 (1416,23200),
 (3000,53990),
 (1985,29990),
 (1534,31490),
 (1427,19899),
 (1380,21200),
 (1494,24250)]

def h_xi(theta0, theta1, x):  # x1,x2代表两个特征量， price forecast（价格预测）
    return theta0 + theta1 * x 

def theta_j(n,j):
    
    if j == 0:
        return h_xi(theta0_guess, theta1_guess, data[n][0]) - data[n][1]
    else:
        return (h_xi(theta0_guess, theta1_guess, data[n][0]) - data[n][1])*data[n][j-1]
variance = 0.0001
alpha = 0.0000001
theta0 = []
theta1 = []
t = []
theta0_guess = 1.
theta1_guess = 1.
# 预测值

theta0_last = 10.
theta1_last = 10.
# 上一个预测值

m = len(data)
i = 0  #计数器
while (abs(theta0_guess - theta0_last) > variance or
        abs(theta1_guess - theta1_last) > variance):
    
    i+=1
    n = random.randint(0,4)
    theta0_last = theta0_guess
    theta1_last = theta1_guess
    
    theta0_guess = theta0_guess - alpha * (1. / m) * theta_j(n,0)
    theta1_guess = theta1_guess - alpha * (1. / m) * theta_j(n,1)
    theta0.append(theta0_guess)
    theta1.append(theta1_guess)
    t.append(i)
print("theta0 第",i,"次迭代", theta0_guess,"\n","theta1 第",i,"次迭代", theta1_guess)
    
#print(theta0)  
plt.subplot(211)
plt.plot(t,theta0)
plt.subplot(212)
plt.plot(t,theta1)




'''
随机梯度下降法(2)一个特征量（for循环）
'''
import random

data = [ (1416.00,  232.000000),
         (1600.00,  330.000000),
         (2104.00,  400.000000),
         (2400.00,  369.000000),
         (3000.00,  540.000000)]

def h_xi(theta0, theta1, x):  # x1,x2代表两个特征量， price forecast（价格预测）
    return theta0 + theta1 * x 

variance = 0.00001
alpha = 0.00000001

theta0_guess = 1.
theta1_guess = 1.
# 预测值

theta0_last = 10.
theta1_last = 10.
# 上一个预测值
m = len(data)
for i in range(500):
    if (abs(theta0_guess - theta0_last) > variance or abs(theta1_guess - theta1_last) > variance):
        i+=1
        theta0_last = theta0_guess
        theta1_last = theta1_guess
    
        n = random.randint(0,4)   
        theta0_guess = theta0_guess - alpha * (1. / m) * (h_xi(theta0_guess, theta1_guess, data[n][0]) - data[n][1])
        
        theta1_guess = theta1_guess - alpha * (1. / m) * ((h_xi(theta0_guess, theta1_guess, data[n][0]) - data[n][1])*data[n][0])
    
        print("theta0 第",i,"次迭代", theta0_guess,"\n","theta1 第",i,"次迭代", theta1_guess)
        
    else:
        print(i+1)



'''
随机梯度下降法(俩特征量（1）)
'''
import random
import matplotlib.pyplot as plt

data = [ (1416.00,3,  232.000000),
         (1600.00,2,  330.000000),
         (2104.00,3,  400.000000),
         (2400.00,5,  369.000000),
         (3000.00,4,  540.000000)]

def h_xi(theta0, theta1,theta2, x1 , x2):  # x1,x2代表两个特征量， price forecast（价格预测）
    return theta0 + theta1 * x1 + theta2 * x2 

def theta_j(n,j):
    
    if j == 0:
        return h_xi(theta0_guess, theta1_guess, theta2_guess, data[n][0], data[n][1]) - data[n][2]
    else:
        return (h_xi(theta0_guess, theta1_guess, theta2_guess, data[n][0], data[n][1]) - data[n][2])*data[n][j-1]
variance = 0.00001
alpha = 0.00000001
theta0 = []
theta1 = []
theta2 = []
t = []
theta0_guess = 1.
theta1_guess = 1.
theta2_guess = 1.
# 预测值

theta0_last = 10.
theta1_last = 10.
theta2_last = 10.
# 上一个预测值

m = len(data)
i = 0  #计数器
while (abs(theta0_guess - theta0_last) > variance or
        abs(theta1_guess - theta1_last) > variance or
        abs(theta2_guess - theta2_last) > variance):
    
    i+=1
    n = random.randint(0,4)
    theta0_last = theta0_guess
    theta1_last = theta1_guess
    theta2_last = theta2_guess
    
    theta0_guess = theta0_guess - alpha * (1. / m) * theta_j(n,0)
    theta1_guess = theta1_guess - alpha * (1. / m) * theta_j(n,1)
    theta2_guess = theta2_guess - alpha * (1. / m) * theta_j(n,2)
    
    theta0.append(theta0_guess)
    theta1.append(theta1_guess)
    theta2.append(theta2_guess)
    t.append(i)
print("theta0 第",i,"次迭代", theta0_guess,"\n","theta1 第",i,"次迭代", theta1_guess,"\n","theta2 第",i,"次迭代", theta2_guess)
    
#print(theta0)  
plt.subplot(311)
plt.plot(t,theta0)
plt.subplot(312)
plt.plot(t,theta1)
plt.subplot(313)
plt.plot(t,theta2)
plt.tight_layout()
plt.show()





'''
随机梯度下降法(俩特征量（2）)
'''
import random
import matplotlib.pyplot as plt

data = [   
 (2104,12,39990),
 (1600, 5,32990),
 (2400,16,36900),
 (1416, 7,23200),
 (3000, 9,53990),
 (1985,25,29990),
 (1534, 3,31490),
 (1427, 1,19899),
 (1380,11,21200),
 (1494,22,24250)]

def h_xi(theta0, theta1,theta2, x1 , x2):  # x1,x2代表两个特征量， price forecast（价格预测）
    return theta0 + theta1 * x1 + theta2 * x2 

def theta_j(n,j):
    
    if j == 0:
        return h_xi(theta0_guess, theta1_guess, theta2_guess, data[n][0], data[n][1]) - data[n][2]
    else:
        return (h_xi(theta0_guess, theta1_guess, theta2_guess, data[n][0], data[n][1]) - data[n][2])*data[n][j-1]
variance = 0.00001
alpha = 0.00000001
theta0 = []
theta1 = []
theta2 = []
t = []
theta0_guess = 1.
theta1_guess = 1.
theta2_guess = 1.
# 预测值

theta0_last = 10.
theta1_last = 10.
theta2_last = 10.
# 上一个预测值

m = len(data)
i = 0  #计数器
while (abs(theta0_guess - theta0_last) > variance or
        abs(theta1_guess - theta1_last) > variance or
        abs(theta2_guess - theta2_last) > variance):
    
    i+=1
    n = random.randint(0,4)
    theta0_last = theta0_guess
    theta1_last = theta1_guess
    theta2_last = theta2_guess
    
    theta0_guess = theta0_guess - alpha * (1. / m) * theta_j(n,0)
    theta1_guess = theta1_guess - alpha * (1. / m) * theta_j(n,1)
    theta2_guess = theta2_guess - alpha * (1. / m) * theta_j(n,2)
    
    theta0.append(theta0_guess)
    theta1.append(theta1_guess)
    theta2.append(theta2_guess)
    t.append(i)

print("theta0 第",i,"次迭代", theta0_guess,"\n","theta1 第",i,"次迭代", theta1_guess,"\n","theta2 第",i,"次迭代", theta2_guess)
    
#print(theta0)  
plt.subplot(311)
plt.plot(t,theta0)
plt.subplot(312)
plt.plot(t,theta1)
plt.subplot(313)
plt.plot(t,theta2)

plt.tight_layout()
plt.show()