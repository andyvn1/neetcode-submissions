class MinStack:

    def __init__(self):
        self.stack = []
        self.min_hold = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_hold[-1] if self.min_hold else val )
        self.min_hold.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_hold.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_hold[-1]
        
