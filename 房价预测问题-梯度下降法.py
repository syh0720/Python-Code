data1 = [(1416.00, 4, 232.000000),
         (1600.00, 3, 330.000000),
         (2104.00, 3, 400.000000),
         (2400.00, 2, 369.000000),
         (3000.00, 5, 540.000000)]

def priceforecast(theta0, theta1, theta2, x1, x2):  # x1,x2代表两个特征量， price forecast（价格预测）

    return theta0 + theta1 * x1 + theta2 * x2
     
if __name__ == '__main__':

    alpha = 0.00000001  # α，学习度要足够小，不然会梯度爆炸，无法显示结果（[nan,nan,nan]）
    variance = 0.00001  # 10的-5次方

    theta0_guess = 1.
    theta1_guess = 1.
    theta2_guess = 1.  # 预测值

    theta0_last = 10.
    theta1_last = 10.
    theta2_last = 10.  # 上一个预测值

    m = len(data1)

    while (abs(theta0_guess - theta0_last) > variance or
           abs(theta1_guess - theta1_last) > variance or
           abs(theta2_guess - theta2_last) > variance):  # 循环结束条件

        theta0_last = theta0_guess
        theta1_last = theta1_guess
        theta2_last = theta2_guess # 更新预测值

        theta0_guess = theta0_guess - alpha * (1. / m) * sum(
            [priceforecast(theta0_guess, theta1_guess, theta2_guess, point[0], point[1]) - point[2] for point in data1])
        theta1_guess = theta1_guess - alpha * (1. / m) * sum(
            [(priceforecast(theta0_guess, theta1_guess, theta2_guess, point[0], point[1]) - point[2]) * point[0] for
             point in data1])
        theta2_guess = theta2_guess - alpha * (1. / m) * sum(
            [(priceforecast(theta0_guess, theta1_guess, theta2_guess, point[0], point[1]) - point[2]) * point[1] for
             point in data1])

    #result = [(float(theta0_guess), float(theta1_guess), float(theta2_guess))]
    print("theta0 = ", theta0_guess,"\n","theta1 = ", theta1_guess,"\n","theta2 = ", theta2_guess)

    X = input("请输入房子面积：")
    Y = input("请输入房子窗户数量：")
    house_price = theta0_guess + theta1_guess * float(X) + theta2_guess * int(Y)
    print("该房子价格预测为：",house_price)