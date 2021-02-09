import numpy as np


def run_affine_transform(A, B, row=True):
    if row:
        p_a = np.ones((3, 3))
        p_b = np.ones((3, 3))

        for i, (x, y) in enumerate(A):
            p_a[i, 0:2] = x, y
        for i, (x, y) in enumerate(B):
            p_b[i, 0:2] = x, y

        print('p_a = \n', p_a)
        print('p_b = \n', p_b)

        m = np.linalg.inv(p_a) @ p_b
        print('m = \n', m)
    else:
        p_a = np.ones((3, 3))
        p_b = np.ones((3, 3))

        for i, (x, y) in enumerate(A):
            p_a[0:2, i] = x, y
        for i, (x, y) in enumerate(B):
            p_b[0:2, i] = x, y

        print('p_a = \n', p_a)
        print('p_b = \n', p_b)

        m = p_b @ np.linalg.inv(p_a)
        print('m = \n', m)


if __name__ == '__main__':
    np.set_printoptions(suppress=True)

    a = [(0, 0), (10, 10), (0, 20)]
    b = [(110, 30), (90, 50), (70, 30)]

    run_affine_transform(a, b, row=True)
    run_affine_transform(a, b, row=False)
