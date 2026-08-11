class Solution:
    def isValid(self, s: str) -> bool:
        valid_p = {")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if c in valid_p:
                if stack and stack[-1] == valid_p.get(c):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

        