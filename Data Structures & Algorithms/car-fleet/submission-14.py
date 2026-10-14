class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key=lambda pair: pair[0], reverse=True)
        # print(f"{cars=}")

        stack = deque() # moves
        fleets = 0

        for pos, spd in cars:
            moves = (target - pos) / spd
            while stack and stack[-1] < moves:
                stack.pop()
            
            if not stack:
                fleets += 1

            stack.append(moves)
            
            # print(f"{moves=}")

        return fleets