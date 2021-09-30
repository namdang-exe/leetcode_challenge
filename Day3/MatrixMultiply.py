# Do other problem in this website
def create_mat(s, m, n):
    out = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            out[i][j] = s
            s += 1

    return out


def multiply(row, column):
    total = 0
    for i in range(len(row)):
        total += row[i] * column[i]
    return total


def multiplyMatrix(s, m, n):
    mat = create_mat(s, m, n)
    out = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(n):
            out[i][j] = multiply(mat[i], mat[j])
    return out


s = 1
m = 3
n = 3
print(multiplyMatrix(s, m, n))
