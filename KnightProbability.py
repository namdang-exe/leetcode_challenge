# 2D Dynamic Programming
# O(n^2 * K) time
# O(n^2) space

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:        
        def in_bound(row, col):
            return 0 <= row < n and 0 <= col < n

        moves = (-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2,1)
        col = column
        dp1 = [[0] * n for _ in range(n)]        
        dp1[row][col] = 1
        
        for i in range(k):
            # using dp1 to update dp2
            # possibly reset dp2 to 0 
            dp2 = [[0] * n for _ in range(n)]
            for row_i in range(n):
                for col_j in range(n):
                    if dp1[row_i][col_j] != 0:
                        # 8 possible positions a knight can move
                        for i,j in moves:
                            if in_bound(row_i+i, col_j+j):
                                # update dp 2
                                dp2[row_i+i][col_j+j] = dp1[row_i][col_j] * 1/8 if not dp2[row_i+i][col_j+j] else dp2[row_i+i][col_j+j] + dp1[row_i][col_j] * 1/8
            dp1 = dp2

        result = 0
        for row in dp1:
            result += sum(row)
            
        return result
        
