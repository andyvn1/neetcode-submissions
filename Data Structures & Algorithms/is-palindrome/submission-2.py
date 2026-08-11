class Solution:
    def isPalindrome(self, s: str) -> bool:
        normal = [c.lower() for c in s if c.isalpha() or c.isdigit()]
        reverse = [normal[i] for i in reversed(range(len(normal)))]
        return normal == reverse
        