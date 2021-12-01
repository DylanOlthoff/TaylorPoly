#Dylan Olthoff
#CST-305
#Project 6
#Ricardo Citro
#packages imported are shown below
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial as fact


def DE1(x):  # Part a
    y0 = 1
    y1 = x
    y2 = - 1 / 2 * pow(x, 2)
    y3 = 1 / 3 * pow(x, 3)
    y4 = -1 / 8 * pow(x, 4)
    return y0 + y1 + y2 + y3 + y4  # return values


def DE2(x):  # Part b
    y0 = 0
    y1 = -1 / fact(1) * x
    y2 = 1 / fact(2) * pow(x, 2)
    y3 = -1 / fact(3) * pow(x, 3)
    y4 = 2 / fact(4) * pow(x, 4)
    return y0 + y1 + y2 + y3 + y4  # return values


def DE3(x, a0, a1):  # Part 2
    a = a0 * (1 - (1 / 8) * pow(x, 2) + (1 / 128) * pow(x, 3) + (1 / 960) * pow(x, 4) - \
              (1 / 15360) * pow(x, 5) - (1 / 161280) * pow(x, 6) - (1 / 26880) * pow(x, 8))
    b = a1 * (x - (1 / 2) * pow(x, 2) - (1 / 6) * pow(x, 3) + (1 / 12) * pow(x, 4) - \
              (1 / 36) * pow(x, 6) + (1 / 224) * pow(x, 7) + (1 / 360) * pow(x, 8))
    return a + b  # return solutions


dt = 0.2  # step size
steps = 5000
xs = np.linspace(-100, 100, steps)
ys1a = np.empty(steps)  #space for part a
ys1b = np.empty(steps)  #space for part b
ys2 = np.empty(steps)  #space for part 2
for i in range(-2500, 2500):
    ys1a[i] = DE1(i * dt)  #values for part 1a
    ys1b[i] = DE2(i * dt)  #values for part 1b
    ys2[i] = DE3(i * dt, 2, 2)  # part 2 values


# Plots and graphs
plt.title("Taylor Series Part1 a")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xs, ys1a)
plt.show()
plt.title("Taylor Series Part1 b")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xs, ys1b)
plt.show()
plt.title("Taylor Series Part 2")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xs, ys2)
plt.show()
