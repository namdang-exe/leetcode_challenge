class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left, max_right, min_lr = [0] * n, [0] * n, [0] * n
        # max_left dp
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i-1])
        # max_right dp
        for i in range(n-1)[::-1]:
            max_right[i] = max(max_right[i+1], height[i+1])
        # min of left and right dp
        for i in range(n):
            min_lr[i] = min(max_left[i], max_right[i])
        # calculate rain
        res = 0
        for i, h in enumerate(height):
            water = min_lr[i] - h
            if water > 0:
                res += water
            
        return res
        
