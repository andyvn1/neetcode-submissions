class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            cnt = len(s)
            output += f"{cnt}#"
            for c in s:
                output += c
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1    
            cnt = int(s[l:r])
            print(s[r + 1:r + 1 + cnt])
            output.append(s[r + 1:r + 1 + cnt])
            l = r + 1 + cnt
        return output

