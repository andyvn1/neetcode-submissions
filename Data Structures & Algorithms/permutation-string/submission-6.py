class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        for c in s1:
            count_s1[c] = 1 + count_s1.get(c, 0)
        
        l = 0
        window_count = {}
        for r in range(len(s2)):
            window_count[s2[r]] = 1 + window_count.get(s2[r], 0)

            if r - l + 1 > len(s1):
                window_count[s2[l]] -= 1
                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]
                l += 1
            if count_s1 == window_count:
                return True
        return False