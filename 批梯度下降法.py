'''
批/梯度下降法（一个特征量，两个特征量的见房价预测问题）
'''
import matplotlib.pyplot as plt
data1 = [(1416.00,  232.000000),
         (1600.00,  330.000000),
         (2104.00,  400.000000),
         (2400.00,  369.000000),
         (3000.00,  540.000000)]
def h_xi(theta0, theta1, x):  # x代表特征量， price forecast（价格预测）
    return theta0 + theta1 * x 

if __name__ == '__main__':
    alpha = 0.00000001  # α，学习度要足够小，不然会梯度爆炸，无法显示结果（[nan,nan,nan]）
    variance = 0.00001  # 10的-5次方
    
    theta0 = []
    theta1 = []
    t = []
    
    theta0_guess = 1.
    theta1_guess = 1.
# 预测值

    theta0_last = 10.
    theta1_last = 10.
# 上一个预测值

    m = len(data1)
    i = 0

    while (abs(theta0_guess - theta0_last) > variance or
            abs(theta1_guess - theta1_last) > variance):
        i+=1
        
        theta0_last = theta0_guess
        theta1_last = theta1_guess
        
        theta0_guess = theta0_guess - alpha * (1. / m) * sum(
                [h_xi(theta0_guess, theta1_guess,  point[0]) - point[1] for point in data1])
        
        theta1_guess = theta1_guess - alpha * (1. / m) * sum(
                [(h_xi(theta0_guess, theta1_guess,  point[0]) - point[1])*point[0] for point in data1])
        
        theta0.append(theta0_guess)
        theta1.append(theta1_guess)
        t.append(i)
    
    print("theta0 第",i,"次迭代", theta0_guess,"\n","theta1 第",i,"次迭代", theta1_guess)       
        
plt.subplot(211)
plt.plot(t,theta0)
plt.subplot(212)
plt.plot(t,theta1)