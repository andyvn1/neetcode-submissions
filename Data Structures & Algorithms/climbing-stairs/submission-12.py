class Solution:
    def climbStairs(self, n: int) -> int:
        before, last = 1, 1
        for i in range(n - 1):
            temp = before
            before = before + last
            last = temp
        return before
        