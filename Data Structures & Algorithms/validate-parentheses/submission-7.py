class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_pair = {"}": "{", ")": "(", "]": "["}

        for c in s:
            if c in valid_pair:
                if stack and stack[-1] == valid_pair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

        