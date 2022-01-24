# recursive approach
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def _helper(numRows):
            if numRows == 0: return []
            if numRows == 1: return [[1]]
            
            row = []
            last = _helper(numRows-1)
            for i in range(numRows):
                if i == 0 or i == numRows-1: row.append(1)
                # case nRow = 3
                # last = [[1], [1,1]]
                else:
                    row.append(last[-1][i-1] + last[-1][i])
            last.append(row)
            return last
        return _helper(numRows)
