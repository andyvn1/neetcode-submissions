class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        t_count = {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)

        l = 0
        window, length = [-1, -1], float("infinity")
        have, musthave = 0, len(t_count)
        window_count = {}
        for r in range(len(s)):
            window_count[s[r]] = 1 + window_count.get(s[r], 0)

            if s[r] in t_count and t_count[s[r]] == window_count[s[r]]:
                have += 1

            while have == musthave:
                if r - l + 1 < length:
                    window, length = [l, r], r - l + 1
                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        
        l, r = window
        return s[l:r + 1]
                

