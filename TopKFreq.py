# Counter method
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        sorted_cnt = sorted(cnt.items(), key=lambda pair:pair[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_cnt[i][0])
        return res
