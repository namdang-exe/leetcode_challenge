# Kadane's algorithm for left and right side
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        
        max_left, max_right, max_sum = [0] * n, [0] * n, [0] * n
        max_right += [0]
        max_left[0], max_sum[0] = arr[0], arr[0]
        
        # max_left dp
        for i in range(1,n):
            num = arr[i]
            max_left[i] = max(max_left[i-1]+num, num)
            max_sum[i] = max(max_sum[i-1], max_left[i])
        # max_right dp
        for i in range(n)[::-1]:
            num = arr[i]
            max_right[i] = max(max_right[i+1]+num, num)
        # res = max(max_left + max_right - num)
        res = arr[0]
        for i in range(1, n):
            res = max(res, max_left[i-1] + max_right[i+1], max_sum[i])
            
        return res
        
