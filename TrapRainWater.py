class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left, max_right = [0] * n, [0] * n
        # max_left dp and max_right dp
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i-1])
            max_right[-i-1] = max(max_right[-i], height[-i])
        # calculate rain
        res = 0
        for i in range(n):
            water = min(max_left[i], max_right[i]) - height[i]
            if water > 0:
                res += water
            
        return res
