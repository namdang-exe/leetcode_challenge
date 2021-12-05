# Kadane's algorithm for left and right side
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        # edge case
        if n == 1: return arr[-1]
        
        max_left, max_right = [0] * (n+2), [0] * (n+2)
        max_left[0], max_right[-1] = 0,0 
        max_left[1], max_right[-2] = arr[0], arr[-1]
        max_sum = [0] * n
        max_sum[0] = arr[0]
        
        # max_left dp
        for i in range(1,n):
            num = arr[i]
            max_left[i+1] = max(max_left[i]+num, num)
            max_sum[i] = max(max_sum[i-1], max_left[i+1])
        # max_right dp
        for i in range(n)[::-1]:
            num = arr[i]
            max_right[i+1] = max(max_right[i+2]+num, num)
        # res = max(max_left + max_right - num)
        res = float('-inf')
        for i in range(n):
            res = max(res, max_left[i] + max_right[i+2], max_sum[i])
            
        return res
        
