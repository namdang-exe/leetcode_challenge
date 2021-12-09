# O(m*n*max(m,n)) time
# O(m*n) space
# Array + hashmap
# {(0,0):0}
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        dict1 = dict()
        # extract zeroes to a hashmap
        # O(m*n)
        for row_i in range(m):
            for col_j in range(n):
                if matrix[row_i][col_j] == 0:
                    dict1[(row_i, col_j)] = 0
        # use the current hashmap
        # to make a new hashmap
        # that has its entire row and columns to 0's
        dict2 = dict()
        # O(m*n*max(m,n))
        for row, col in dict1.keys():
            for row_i in range(m):
                dict2[(row_i, col)] = 0
            for col_j in range(n):
                dict2[(row, col_j)] = 0
        # O(m*n)
        for row_i in range(m):
            for col_j in range(n):
                if (row_i, col_j) in dict2:
                    matrix[row_i][col_j] = dict2[(row_i, col_j)]
