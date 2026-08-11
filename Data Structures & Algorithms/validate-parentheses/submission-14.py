class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_dic = {")": "(", "]":"[", "}":"{"}

        for c in s:
            if c in valid_dic:
                if stack and valid_dic[c] == stack[-1]:
                    stack.pop()
                else:
                    return False            
            else:
                stack.append(c)
        return len(stack) == 0
        