import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def update_wave1(val):
    global frequency1, amplitude1
    frequency1 = slider_frequency1.val
    amplitude1 = slider_amplitude1.val
    update_plot()


def update_wave2(val):
    global frequency2, amplitude2
    frequency2 = slider_frequency2.val
    amplitude2 = slider_amplitude2.val
    update_plot()


def update_plot():
    t = np.linspace(0, 2 * np.pi, 1000)
    wave1 = amplitude1 * np.sin(2 * np.pi * frequency1 * t)
    wave2 = amplitude2 * np.sin(2 * np.pi * frequency2 * t)

    ax_wave1.clear()
    ax_wave1.plot(t, wave1)
    ax_wave1.set_title('Волна 1')

    ax_wave2.clear()
    ax_wave2.plot(t, wave2)
    ax_wave2.set_title('Волна 2')

    ax_result.clear()
    ax_result.plot(t, wave1 + wave2)
    ax_result.set_title('Волна 1 + Волна 2')

    plt.draw()


fig, (ax_wave1, ax_wave2, ax_result) = plt.subplots(3, 1, figsize=(12, 9))
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.4, top=0.9, hspace=0.5)

frequency1 = 1.0
amplitude1 = 1.0

frequency2 = 1.0
amplitude2 = 1.0

axfreq1 = plt.axes([0.25, 0.25, 0.65, 0.03])
slider_frequency1 = Slider(axfreq1, 'Частота 1', 0.1, 10.0, valinit=frequency1)
slider_frequency1.on_changed(update_wave1)
axamp1 = plt.axes([0.25, 0.2, 0.65, 0.03])
slider_amplitude1 = Slider(axamp1, 'Амплитуда 1', 0.1, 5.0, valinit=amplitude1)
slider_amplitude1.on_changed(update_wave1)

axfreq2 = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_frequency2 = Slider(axfreq2, 'Частота 2', 0.1, 10.0, valinit=frequency2)
slider_frequency2.on_changed(update_wave2)
axamp2 = plt.axes([0.25, 0.05, 0.65, 0.03])
slider_amplitude2 = Slider(axamp2, 'Амплитуда 2', 0.1, 5.0, valinit=amplitude2)
slider_amplitude2.on_changed(update_wave2)

plt.show()
