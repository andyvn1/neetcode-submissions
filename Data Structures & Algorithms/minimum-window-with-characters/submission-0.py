class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        t_count, window_count = {}, {}

        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        l = 0
        have, must_have = 0, len(t_count)
        substring, length = [-1, -1], float("infinity")
        for r in range(len(s)):
            c = s[r]
            window_count[c] = 1 + window_count.get(c, 0)

            if c in t_count and window_count[c] == t_count[c]:
                have += 1
            
            while have == must_have and l <= r:
                if (r - l + 1)  < length:
                    substring, length = [l, r], min(length, r - l + 1)

                left_c = s[l]
                window_count[left_c] -= 1
                if left_c in t_count and window_count[left_c] < t_count[left_c]:
                    have -= 1
                
                l += 1
        l, r = substring
        return s[l:r + 1]


        