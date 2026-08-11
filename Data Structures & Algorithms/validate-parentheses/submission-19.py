class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_ones = {"}": "{", "]": "[", ")": "("}
        for c in s:
            if c in valid_ones:
                if stack and stack[-1] == valid_ones[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
        