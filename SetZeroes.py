# using sets
# a set of rows
# a set of columns
# mark infected rows and columns
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        cols = set()
        for row_i in range(m):
            for col_j in range(n):
                if matrix[row_i][col_j] == 0:
                    rows.add(row_i)
                    cols.add(col_j)
        
        for row_i in range(m):
            for col_j in range(n):
                if row_i in rows or col_j in cols:
                    matrix[row_i][col_j] = 0
                    
                    
