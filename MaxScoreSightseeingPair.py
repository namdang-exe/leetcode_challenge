# dynamic programming
# 2 parts: A[i] + i + A[j] - j 
# dp1 for A[i] + i
# dp2 for dp1 + A[j] - j
# note: update dp2 before dp1 bc we want to skip the last element of dp1 
# which is the end aka no sightseeing
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_so_far = values[0]
        result = 0
        for i in range(1, len(values)):
            result = max(result, max_so_far + values[i] - i)
            max_so_far = max(max_so_far, values[i] + i)
            
        return result
