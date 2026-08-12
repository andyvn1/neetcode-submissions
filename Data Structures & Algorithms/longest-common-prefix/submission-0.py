class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        min_c = len(min(strs))
        failed = False
        for c in range(min_c):
            match = ""
            for i in range(len(strs)):
                word = strs[i]
                if i == 0:
                    match += word[c]
                else:
                    if word[c] != match:
                        match = ""
                        failed = True
            if failed == True:
                break
            output += match
        return output

      