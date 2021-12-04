# Brute Force
# O(n^3) time
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        team = 0
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        team += 1
        return team
