class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while not self.isalphanum(s[l]) and l < r:
                l += 1
            while not self.isalphanum(s[r]) and l < r:
                r -= 1
            if s[l].lower() == s[r].lower() and l < r:
                l, r = l + 1, r - 1
            elif s[l].lower() == s[r].lower() and l == r:
                return True
            else:
                return False
        return True



    def isalphanum(self, n):
        return (ord('a') <= ord(n.lower()) <= ord('z') or 
                ord('0') <= ord(n) <= ord('9'))
        