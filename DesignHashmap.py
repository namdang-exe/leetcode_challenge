class MyHashMap:

    def __init__(self):
        self.items = [] # [[k,v]]

    def put(self, key: int, value: int) -> None:
        found = False
        for i in range(len(self.items)):
            k, v = self.items[i]
            if k == key:
                found = True
                self.items[i] = [key, value]
        if not found:        
            self.items.append([key, value])

    def get(self, key: int) -> int:
        "O(n) time"
        for k, v in self.items:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for k, v in self.items:
            if k == key:
                self.items.remove([k, v])


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
