class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            count = len(word)
            output += f"{count}#"
            for c in word:
               output += c 
        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        s_list = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1
            count = int(s[l:r])
            s_list.append(s[r + 1: r + 1 + count])
            l = r + 1 + count
        return s_list




