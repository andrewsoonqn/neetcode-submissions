from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        
    def push(self, val: int) -> None:
        s = self.stack
        if s:
            mn = min(s[-1][1], val)
            s.append((val, mn))
        else:
            s.append((val, val))


    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

        
