import matplotlib.pyplot as plt
w1 = 0
w2 = 0
a = 0
b = 10
N = 100
h = (b-a)/N

w1_list = []
w2_list = []
x_list = []

def f1(I1, I2):
    return (-4)*I1 + 3*I2 + 6
def f2(I1, I2):
    return (-2.4)*I1 + 1.6*I2 + 3.6


for j in range(N):
    t = a + j*h
    
    x_list += [t]
    w1_list += [w1]
    w2_list += [w2]
    
    k1_1 = h*f1(w1, w2)
    k1_2 = h*f1(w1+k1_1/2, w2+k1_1/2)
    k1_3 = h*f1(w1+k1_2/2, w2+k1_2/2)
    k1_4 = h*f1(w1+k1_3, w2+k1_3)
    
    w1 = w1 + (k1_1 + 2*k1_2 + 2*k1_3 + k1_4)/6
    
    
    k2_1 = h*f2(w1, w2)
    k2_2 = h*f2(w1+k2_1/2, w2+k2_1/2)
    k2_3 = h*f2(w1+k2_2/2, w2+k2_2/2)
    k2_4 = h*f2(w1+k2_3, w2+k2_3)
    
    w2 = w2 + (k2_1 + 2*k2_2 + 2*k2_3 + k2_4)/6
    
plt.plot(x_list, w2_list, 'r')
plt.plot(x_list, w1_list, 'b')
plt.show()