class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        nums = []

        for t in tokens:
            if t in "+-*/":
                b = nums.pop()   # top of the stack (right side)
                a = nums.pop()   # next one down (left side)

                if t == "+":
                    nums.append(a + b)
                elif t == "-":
                    nums.append(a - b)
                elif t == "*":
                    nums.append(a * b)
                else:
                    nums.append(int(a / b))  # truncate toward zero
            else:
                nums.append(int(t))

        return nums[0]