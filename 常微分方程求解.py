import matplotlib.pyplot as plt
import numpy as np
#diff(y) = y - 2*x/y
y = [1]
x = [0]
x1 = np.arange(0,1,0.001)
y1 = (x1*x1/ x1 - 0.5) ** 0.5
for i in range(10):
    h = 0.1
    
    x.append(x[i] + h)
    y.append(y[i] + h * (y[i] - 2*x[i]/y[i]))
    #y.append(1.1*y[i] - 0.2 * x[i]/y[i])
#     print(x)
#     print(y)
plt.subplot(211)
plt.plot(x,y,'ro-', color='blue', alpha=0.8, linewidth=1)
plt.subplot(212)
plt.plot(x1,y1)