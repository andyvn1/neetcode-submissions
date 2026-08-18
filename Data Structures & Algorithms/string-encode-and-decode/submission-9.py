class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            count = len(word)
            output += f"{count}#{word}"
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1
            count = int(s[l:r])
            substring = s[r + 1: r + count + 1]
            output.append(substring)
            l = r + count + 1
        return output

