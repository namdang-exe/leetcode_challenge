class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        # O(n)
        for s, e in intervals:
            start.append(s)
            end.append(e)
        # O(nlogn)
        start.sort()
        end.sort()
        # start: [0,5,15]
        # end: [10,20,30]
        res, count = 0, 0
        i, j = 0, 0
        # O(n)
        while i < len(start):
            # they are equal, we prioritize the end array
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)
            
        return res
            
