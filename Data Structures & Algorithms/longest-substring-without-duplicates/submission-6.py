class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        no_duplicates = set()
        count = 0
        l = 0
        for r in range(len(s)):
            while s[r] in no_duplicates:
                no_duplicates.remove(s[l])
                l += 1
            no_duplicates.add(s[r])
            count = max(count, (r - l) + 1)
        return count

       