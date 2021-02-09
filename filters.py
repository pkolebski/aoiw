import numpy as np
from scipy.ndimage import minimum_filter, median_filter, maximum_filter


def run_filter(image, filter, size):
    print(filter(image, size))


if __name__ == '__main__':
    image = np.array([
        [.4, .5, .9, .1, .3],
        [1., .7, .8, .1, .2],
        [.8, .5, .6, .0, .1],
        [.5, .2, .1, .2, .9],
        [.1, .9, .2, .5, .4],
    ])
    # minimum_filter,
    # median_filter,
    # maximum_filter
    run_filter(image, median_filter, size=3)
