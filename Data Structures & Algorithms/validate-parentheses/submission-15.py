class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_dic = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c in valid_dic:
                if stack and stack[-1] == valid_dic[c]:
                    stack.pop()
                else:
                    return False            
            else:
                stack.append(c)
        return len(stack) == 0

        