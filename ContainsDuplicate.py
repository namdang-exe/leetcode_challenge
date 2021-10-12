# hashmap
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
            if hash_map[num] == 2:
                return True
        return False
