class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        t_count, window_count = {}, {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        have, must_have = 0, len(t_count)
        substring, substring_length = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            right_c = s[r]
            window_count[right_c] = 1 + window_count.get(right_c, 0)

            if right_c in t_count and window_count[right_c] == t_count[right_c]:
                have += 1

            while have == must_have and l <= r:

                if (r - l + 1) < substring_length:
                    substring, substring_length = [l, r], r - l + 1

                left_c = s[l]
                window_count[left_c] -= 1

                if left_c in t_count and window_count[left_c] < t_count[left_c]:
                    have -= 1

                l += 1
        l, r = substring
        return s[l: r+ 1]
            


            
