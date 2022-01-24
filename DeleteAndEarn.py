# DP
# Make an array to keep track of the frequency
# Then the problem turned into House Robber
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # create an array for frequency
        # since the number +1 and number - 1 are deleted
        # which means we can't add their value
        # this is similar to the neighbor constraint in House Robber problem
        m = max(nums) + 1
        freq = [0] * m
        for n in nums:
            freq[n] += 1
        # TODO: edge cases
        
        # DP
        # two pointers
        one, two = 0, 0
        for i in range(1, m):
            max_points = max(freq[i]*i + one, two)
            one = two
            two = max_points
            
        return two
        
