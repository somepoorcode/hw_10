import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def lissajous_figure(a, b, delta):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = np.sin(a * t + delta)
    y = np.sin(b * t)

    plt.plot(x, y)
    plt.title(f'Фигура Лисажу ({a}:{b})')

    plt.grid(True)
    plt.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False)
    plt.axis('on')


def update(frame):
    ax.clear()
    frequency_ratio = frame / 100
    lissajous_figure(3, 2 + frequency_ratio, 0)


fig, ax = plt.subplots()

ani = FuncAnimation(fig, update, frames=100, interval=60)

plt.show()
