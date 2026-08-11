class Solution:
    def isValid(self, s: str) -> bool:
        valid_bra = {")": "(", "]":"[", "}": "{"}
        stack = []
        for c in s:
            if c in valid_bra:
                if stack and stack[-1] == valid_bra[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0