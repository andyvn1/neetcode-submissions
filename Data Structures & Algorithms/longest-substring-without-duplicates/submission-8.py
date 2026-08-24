class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        no_duplicate = set()
        l = 0
        output = 0

        for r in range(len(s)):
            while s[r] in no_duplicate:
                no_duplicate.remove(s[l])
                l += 1
            no_duplicate.add(s[r])
            output = max(output, r - l + 1)
        return output

        