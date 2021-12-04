# More optimal solution
# O(n^2) time

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        team = 0
        for i in range(n):
            inc1, inc3, des1, des3 = 0,0,0,0
            for j in range(n):
                if j < i:
                    if rating[j] > rating[i]:
                        des1 += 1
                    else:
                        inc1 += 1
                if j > i:
                    if rating[j] > rating[i]:
                        inc3 += 1
                    else:
                        des3 += 1
            team += (des1*des3)
            team += (inc1*inc3)
            
        return team
