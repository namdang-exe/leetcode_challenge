class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Construct hash table
        order = list(order)
        hash_table = {}
        for i in range(len(order)):
            hash_table[order[i]] = i
        sorted_words = sorted(words, key=lambda word:[hash_table.get(letter) for letter in word])
        if sorted_words != words:
            return False
        else:
            return True
