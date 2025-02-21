import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, num=100)
y = np.sin(x)

plt.plot(x, y)

plt.show()

print(np.linspace(15, 55, 10, retstep=True))
