from scipy.ndimage import binary_closing, binary_dilation, binary_erosion, \
    binary_fill_holes, binary_opening, binary_propagation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


def run_binary_morphology(image, filter, morphology_type):
    def plot_subplot(data, axe):
        cmap = colors.ListedColormap(['red', 'blue'])
        bounds = [0, 10, 20]
        norm = colors.BoundaryNorm(bounds, cmap.N)

        axe.imshow(data * 255, cmap=cmap, norm=norm)
        axe.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        axe.set_xticks(np.arange(-.5, data.shape[0], 1))
        axe.set_yticks(np.arange(-.5, data.shape[1], 1))

    fig, ax = plt.subplots(1, 3)
    plot_subplot(image, ax[0])
    plot_subplot(filter, ax[1])
    plot_subplot(morphology_type(image, filter), ax[2])
    plt.show()


if __name__ == '__main__':
    image = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    filter = np.array([
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
    ])

    # binary_closing
    # binary_dilation
    # binary_erosion
    # binary_fill_holes
    # binary_opening
    # binary_propagation
    run_binary_morphology(image, filter, binary_erosion)