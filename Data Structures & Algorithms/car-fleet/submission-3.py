class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars]

        stack = []
        
        for time in times:
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)