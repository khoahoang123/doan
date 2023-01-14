import matplotlib.pyplot as plt
import numpy as np
from sympy import *

x = symbols('x')
def ham_bac_4():
    b4 = x**4-2*x**2-3
    return b4
def ham_bac_3():
    b3 = 4*x**3 - 4*x
    return b3
def ham_bac_2():
    b2 = 12*x**2 - 4
    return b2
def ham_bac_1():
    b1 = 24*x
    return b1

fig,(ax) = plt.subplots()
x = np.linspace(-20,20,20)
y4=ham_bac_4()
ax.plot(x,y4, '*-', label = r"$y$")
y3=ham_bac_3()
ax.plot(x,y3, 'D-', label = r"$y'$")
y2=ham_bac_2()
ax.plot(x,y2, 'ro-', label = r"$y''$")
y1=ham_bac_1()
ax.plot(x,y1, 'g^-', label = r"$y'''$")
ax.set_title("do thi phuong trinh bac 1,2,3,4")
ax.set_xlabel("trục hoành - x")
ax.set_xlabel("trục tung - y")
ax.legend()
plt.show()
