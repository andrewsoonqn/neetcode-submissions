from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = deque()

        def operate(op, a, b):
            return a + b \
                if op == "+" \
                else a - b \
                if op == "-" \
                else a * b \
                if op == "*" \
                else int(a / b) # truncate twd 0

        for tk in tokens:
            if tk in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(operate(tk, a, b))
            else:
                stack.append(int(tk))
            
        return int(stack.pop())