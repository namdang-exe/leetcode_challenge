import numpy as np


def matrixMulti(s, m, n):
    mat = np.array(cons_mat(s, m, n))
    mat_trans = np.transpose(mat)
    # print(mat)
    # print(mat_trans)
    return np.matmul(mat, mat_trans)


def cons_mat(s, m, n):
    # construct matrix
    # [[4, 5], [6, 7], [8, 9]]
    mat = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp += [s]
            s += 1
        mat.append(temp)
    return mat


def multi(row, col):
    m = len(row)
    res = 0
    for i in range(m):
        res += row[i] * col[i]
    return res


def construct_transpose(mat, m, n):
    transpose = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            transpose[i][j] = mat[j][i]
    return transpose


def multi_transpose(mat, m):
    out = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            out[i][j] = multi(mat[i], mat[j])
    return out


def matMulti(s, m, n):
    mat = cons_mat(s, m, n)
    T = construct_transpose(mat, m, n)
    out = multi_transpose(mat, m)
    return out


# test = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
test2 = np.array([[1, 2], [3, 4]])
# test1 = [[1, 2], [3, 4]]
test = [[4, 5], [6, 7], [8, 9]]
print(matrixMulti(4, 3, 2))
print(matMulti(4, 3, 2))
