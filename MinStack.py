class MinStack:

    def __init__(self):
        self.items = []
        

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1] if len(self.items) != 0 else None

    def getMin(self) -> int:
        return min(self.items) if len(self.items) != 0 else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
