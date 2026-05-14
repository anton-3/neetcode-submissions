class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for pos, s in cars:
            time = (target - pos) / s
            if len(stack) == 0 or stack[-1] < time:
                stack.append(time)
        return len(stack)