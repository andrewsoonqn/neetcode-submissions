class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack_r = deque() # h, i
        r_bound = [n] * n
        
        for i, h in enumerate(heights):
            while stack_r and stack_r[-1][0] > h:
                h2, i2 = stack_r.pop()
                r_bound[i2] = i

            stack_r.append((h, i))

        # print(f"{r_bound=}")

        stack_l = deque() # h, i
        l_bound = [-1] * n
        
        for i in reversed(range(n)):
            h = heights[i]
            while stack_l and stack_l[-1][0] > h:
                h2, i2 = stack_l.pop()
                l_bound[i2] = i

            stack_l.append((h, i))

        # print(f"{l_bound=}")

        mx = -1
        for i in range(n):
            width = r_bound[i] - l_bound[i] - 1
            area = width * heights[i]
            # print(f"{area=} {width=}xheight={heights[i]}")
            mx = max(mx, area)
        
        return mx