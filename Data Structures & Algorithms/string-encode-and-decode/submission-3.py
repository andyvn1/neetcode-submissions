class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            count = len(word)
            output += f"{count}#"
            for c in word:
                output += c
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        l = 0

        while l < len(s):
            j = l
            while s[j] != '#':
                j += 1
            n = int(s[l:j])
            l = j + 1
            
            output.append(s[l: l + n])
            l = l + n           
        return output

