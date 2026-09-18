class MinStack:

    def __init__(self):
        self.stack = []
        self.min_v = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(self.min_v[-1] if self.min_v else val, val)
        self.min_v.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_v.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.min_v[-1] if self.min_v else None
        
