import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

x = np.linspace(-1, 1, 100)

plt.figure(figsize=(8, 6))

for n in range(1, 8):
    y = legendre(n)(x)
    plt.plot(x, y, label=f'n = {n}')

plt.title('Полиномы Лежандра')
plt.xlabel('x')
plt.ylabel('P_n(x)')
plt.legend(loc='lower right')

plt.grid(True)
plt.show()
