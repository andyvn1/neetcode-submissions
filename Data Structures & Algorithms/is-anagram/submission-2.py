from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_word = dict(Counter(s))
        t_word = dict(Counter(t))

        return s_word == t_word
        