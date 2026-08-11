class Solution:
    def climbStairs(self, n: int) -> int:
        lastStep = 1
        before = 1

        for i in range(n - 1):
            temp = before
            before = lastStep + before
            lastStep = temp
        return before

        