class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Mapset = set()
        L, res = 0, 0

        for R in range(len(s)):
            while s[R] in Mapset:
                Mapset.remove(s[L])
                L += 1
            res = max(res, R - L + 1)
            Mapset.add(s[R])
        return res
        