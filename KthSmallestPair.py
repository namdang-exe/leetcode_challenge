# Brute force
# O(n^2)
# O(n^2 + nlogn + k)
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        indices = [] # (sum, idx1, idx2)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                cur_sum = nums1[i] + nums2[j]
                indices.append((cur_sum, i, j))
        indices.sort(key=lambda items:items[0])
        res = []
        for i in range(k):
            # edge case
            if i < len(indices):
                res.append([nums1[indices[i][1]], nums2[indices[i][2]]])
        return res
