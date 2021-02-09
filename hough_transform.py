import numpy as np
import matplotlib.pyplot as plt


def run_hough_transform(x, y, min_x, max_x):
    def fun(theta):
        return np.cos(np.deg2rad(theta)) * x + np.sin(np.deg2rad(theta)) * y

    plot_x = np.linspace(min_x, max_x, 200)
    plot_y = [fun(i) for i in plot_x]
    plt.plot(plot_x, plot_y)
    plt.show()


run_hough_transform(14, 14, -45, 140)
