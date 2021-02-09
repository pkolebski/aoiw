from typing import Tuple

# A----F--B
# |    |  |
# |----x--|
# |    |  |
# C----E--D


def run_two_line_interpolation(a: Tuple[Tuple[int, int], int],
                               b: Tuple[Tuple[int, int], int],
                               c: Tuple[Tuple[int, int], int],
                               d: Tuple[Tuple[int, int], int],
                               new_point: Tuple[int, int]):
    f = ((b[0][0] - new_point[0]) / (b[0][0] - a[0][0])) * (a[1] - b[1]) + b[1]
    e = ((d[0][0] - new_point[0]) / (d[0][0] - c[0][0])) * (c[1] - d[1]) + d[1]
    x = ((c[0][1] - new_point[1]) / (c[0][1] - a[0][1])) * (f - e) + e
    return x


if __name__ == '__main__':
    a = ((4, 12), 140)
    b = ((12, 12), 70)
    c = ((4, 4), 10)
    d = ((12, 4), 0)
    print(run_two_line_interpolation(a, b, c, d, (6, 9)))
