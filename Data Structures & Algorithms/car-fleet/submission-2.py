class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # closest to target first
        stack = []  # each entry is the arrival time of a fleet

        for p, s in cars:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)  # can't catch the fleet ahead, so it's a new fleet
            # otherwise it catches up and joins the fleet ahead, so don't push

        return len(stack)