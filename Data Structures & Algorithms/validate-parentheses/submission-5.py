class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair_dic = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in pair_dic:
                if stack and stack[-1] == pair_dic[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

        