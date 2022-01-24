# Binary search
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        l,r = 0, n-1
        res = 0
        while l <= r:
            m = (l+r)//2
            # if citations[m] == n - m: we found the target

            if citations[m] == n - m:
                return m
            # if citations[m] < n - m: we can do better
            # ignore the left side
            # searching right side
            elif citations[m] < n - m:
                l = m + 1
            # if citations[m] > n - m
            # we ignore the right side
            # go to the left side 
            else: # m > n -m
                r = m - 1
                
        return res
                
