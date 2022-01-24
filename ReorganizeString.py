# get rid of the most frequent letter
# build a max heap
# get rid of the max freq
# decrease the freq
# if freq > 0, put in the heap again
# have a pointer to keep track of
# the letter we just popped

from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # dict to keep track of frequency
        cnt = Counter(s)
        # build a max heap
        max_heap = [(-freq, letter) for letter, freq in cnt.items()]
        heapq.heapify(max_heap)
        
        res = []
        previous_letter = None
        previous_freq = 0
        while max_heap:
            freq, letter = heapq.heappop(max_heap)
            res.append(letter)
            freq += 1
            # this will return the correctly organized string
            # the leftover will not be touched
            if previous_freq < 0:
                heapq.heappush(max_heap, (previous_freq, previous_letter))
            previous_letter = letter
            previous_freq = freq
        return "".join(res) if len(res) == len(list(s)) else ""
                        
        
        
        
