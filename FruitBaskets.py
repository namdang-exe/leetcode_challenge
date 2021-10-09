# Sliding window O(n) time and O(k) space sol
# since k = 2 => O(1) space complexity
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = float('-inf')
        unique_f = dict()
        start = 0
        for end, fruit in enumerate(fruits):
            unique_f[fruit] = unique_f.get(fruit, 0) + 1
            # check for unique fruit in the dict
            while len(unique_f) > 2:
                unique_f[fruits[start]] -= 1
                if unique_f[fruits[start]] == 0:
                    unique_f.pop(fruits[start])
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len
