from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        closes = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for ch in s:
            if ch in closes:
                if stack and closes[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
            
        if stack:
            return False
        return True

            