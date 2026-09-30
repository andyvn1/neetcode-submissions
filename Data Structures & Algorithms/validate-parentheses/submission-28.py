class Solution:
    def isValid(self, s: str) -> bool:
        parentesis_dict = {']':'[', ')':'(', '}': '{'}
        stack = []

        for c in s:
            if c in parentesis_dict:
                if stack and stack[-1] == parentesis_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0