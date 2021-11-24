# Brute force
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        for i in range(len(values)):
            for j in range(i+1,len(values)):
                cur_score = values[i] + values[j] + i - j
                max_score = max(max_score, cur_score)
                
        return max_score
