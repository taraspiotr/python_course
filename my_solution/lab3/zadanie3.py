import numpy as np


def reduce(object, size):
        if isinstance(size, tuple):
                if len(size) == 2 and isinstance(size[1], int) and isinstance(
                    size[0], int):
                        reduce_m, reduce_n = size
                else:
                        print "Zle dane"
                        return
        elif isinstance(size, int):
                reduce_m, reduce_n, = size, size
        else:
                print "Zle dane"
                return

        m, n = object.shape
        if reduce_m > m or reduce_n > n or (reduce_m == m and reduce_n == n):
                print "Zle dane"
                return

        mat = np.zeros([reduce_m, reduce_n])

        prop_height = float(m + 1) / reduce_m
        prop_width = float(n + 1) / reduce_n

        for (x, y), element in np.ndenumerate(mat):

                p = int(x * prop_height)
                q = int(y * prop_width)

                counter = 1
                temp = object[p][q]

                # print p, q, x, y

                for (i, j) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        h = p + i
                        w = q + j
                        # print h, w
                        if 0 <= h < m and 0 <= w < n:
                                temp += object[h][w]
                                counter += 1
                                # print counter
                mat[x][y] = float(temp) / counter

        return mat
