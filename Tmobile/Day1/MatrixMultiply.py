"""
Not optimized
"""


def create_mat(s, m, n):
    mat = [[0] * n for _ in range(m)]
    # m = 3, n = 2
    # [[0,0], [0,0], [0,0]]
    for i in range(m):
        for j in range(n):
            mat[i][j] = s
            s += 1
    return mat


def multiply(first, second):
    # [1,2,3] * [4,5,6]
    # 1*4 + 2*5 + 3*6
    total = 0
    for i in range(len(first)):
        total = total + first[i] * second[i]
    return total


def matrixMult(s, m, n):
    # Create a matrix
    mat = create_mat(s, m, n)
    # Calculate the output matrix
    # Multiplying transpose matrix means multiply itself
    result = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            result[i][j] = multiply(mat[i], mat[j])
    return result


print(matrixMult(1, 3, 3))
