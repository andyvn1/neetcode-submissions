class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output += f"{len(word)}#{word}"
        return output

    def decode(self, s: str) -> List[str]:
        word_list = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1
            count = int(s[l:r])
            word = s[r + 1: r + count + 1]
            word_list.append(word)
            l = r + count + 1
        return word_list
