class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # shift a by 1 ----> aka b
        
        # ord('a') - ord('a') ----> 0
        # 0 + 1 ----> 1 , need to wrap around % 26
        # 1 + 97 ----> 98 ----> 'b'
        # chr((ord(c) - ord('a') + shift)%26 + ord('a'))
        
        # [3,5,9]
        # [9,5,3]
        # [9, 14, 17]
        # [17, 14, 9]
        
        shifts = list(accumulate(shifts[::-1]))[::-1]
        s = list(s)
        for i, shift in enumerate(shifts):
            s[i] = chr((ord(s[i]) - ord('a') + shift)%26 + ord('a'))
                
        return ''.join(s)
