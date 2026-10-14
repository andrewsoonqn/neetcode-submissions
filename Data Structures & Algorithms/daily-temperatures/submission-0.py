class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = deque() # (tp, i)

        for i, tp in enumerate(temperatures):
            while stack and stack[-1][0] < tp:
                _, s_i = stack.pop()
                result[s_i] = i - s_i
            
            stack.append((tp, i))
        
        while stack:
            _, i = stack.pop()
            result[i] = 0
        
        return result