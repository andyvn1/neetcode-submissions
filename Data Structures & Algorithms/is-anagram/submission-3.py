class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for c in s:
            dict_s[c] = 1 + dict_s.get(c, 0)
        
        dict_t = {}
        for c in t:
            dict_t[c] = 1 + dict_t.get(c, 0)
        
        return dict_s == dict_t
        