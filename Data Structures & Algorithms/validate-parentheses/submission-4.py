class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair_dic = {"]":"[", "}":"{", ")":"("}
        
        for char in s:
            if char in pair_dic:
                if stack and stack[-1] == pair_dic[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack
        