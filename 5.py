import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 16)
y = np.linspace(-2, 2, 16)
x, y = np.meshgrid(x, y)
z = np.random.rand(*x.shape) * 2

mse = np.sqrt(np.square(z - np.mean(z)))

fig = plt.figure(figsize=(10, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x, y, mse, cmap='viridis')
ax1.set_title('MSE')
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x, y, np.log1p(mse), cmap='plasma')
ax2.set_title('MSE с логарифмической шкалой по z')

plt.show()
