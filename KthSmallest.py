# Brute force
# Flatten the matrix into an array
# Time: O(n**2)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # index of row
        res = []
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                res.append(matrix[r][c])
        return sorted(res)[k-1]
