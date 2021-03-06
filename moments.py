import numpy as np


def run_regular_moments(image, p, q):
    mpq = 0
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j] == 1:
                mpq += (i ** p) * (j ** q)
    return mpq


def run_central_moments(image, p, q, normalize=False):
    m00 = np.sum(image)
    x_ = run_regular_moments(image, 1, 0) / m00
    y_ = run_regular_moments(image, 0, 1) / m00
    mpq = 0
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j] == 1:
                mpq += ((i - x_) ** p) * ((j - y_) ** q)
    if normalize:
        gamma = (p + q + 2) / 2
        return mpq / (run_central_moments(image, 0, 0, normalize=False) ** gamma)
    return mpq


if __name__ == '__main__':
    image = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ])

    print(run_central_moments(image, 3, 0, True))