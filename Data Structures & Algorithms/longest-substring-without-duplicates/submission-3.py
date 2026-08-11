class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L, result = 0, 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            result = max(result, R - L + 1)    
            window.add(s[R])
        return result       