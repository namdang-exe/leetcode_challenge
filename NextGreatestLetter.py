# bin search
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        low, high = 0, len(letters) - 1
        while low < high:
            mid = (low+high) // 2
            # ignore the second half
            if letters[mid] > target:
                # why is this not mid - 1 ???
                # Because if  "d" > "c" e.g
                # d might be the result
                high = mid
            # ignore the first half
            else:
                low = mid + 1
        return letters[low]
