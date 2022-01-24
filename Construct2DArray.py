class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        counter = 0
        for i in range(m):
            row_i = []
            for j in range(n):
                if counter >= len(original): return [] 
                row_i.append(original[counter])
                counter += 1
            res.append(row_i)
        return [] if counter != len(original) else res
