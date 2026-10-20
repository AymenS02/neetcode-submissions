class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ch in s:
            if ch in pairs:                              # closer
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:                                        # opener
                stack.append(ch)

        return not stack 