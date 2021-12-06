# use hashmap to store all scores of IDs
# scores are stored in a list []
# sort list []
# print the average of top 5
# Time complexity: O(n) + O(i * slog(s))

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        db = dict() # {ID:[]} {1:[100,85]}
        for ID, score in items: # O
            db[ID] = db.get(ID, []) + [score]
        res = []
        for k in db.keys(): # O(i)
            top_five = sorted(db[k], reverse=True)[:5]
            avg = sum(top_five)//5
            res.append([k, avg])
        return sorted(res, key=lambda pairs:pairs[0])
