# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import matplotlib.pyplot as plt
import numpy as np

x, y, y1 = np.loadtxt('20230217.txt', delimiter=';', unpack=True)
plt.plot(x,(y/10),(y1/10), label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
