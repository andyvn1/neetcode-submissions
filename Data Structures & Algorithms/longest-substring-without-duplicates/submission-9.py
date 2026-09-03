class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        no_duplicate = set()
        l, max_count = 0, 0

        for r in range(len(s)):
            while s[r] in no_duplicate:
                no_duplicate.remove(s[l])
                l += 1
            max_count = max( r - l + 1, max_count)
            no_duplicate.add(s[r])
            
        return max_count
        
        