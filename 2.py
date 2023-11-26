import numpy as np
import matplotlib.pyplot as plt


def lissajous_figure(a, b, delta):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = np.sin(a * t + delta)
    y = np.sin(b * t)

    plt.plot(x, y)
    plt.title(f'Фигура Лисажу ({a}:{b})')

    plt.grid(True)
    plt.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False)
    plt.axis('on')


plt.figure(figsize=(6, 5))

plt.subplot(221)
lissajous_figure(3, 2, 0)

plt.subplot(222)
lissajous_figure(3, 4, 0)

plt.subplot(223)
lissajous_figure(5, 4, 0)

plt.subplot(224)
lissajous_figure(5, 6, 0)

plt.tight_layout()
plt.show()
