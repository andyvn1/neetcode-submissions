class Solution:
    def climbStairs(self, n: int) -> int:
        lastNum = 1
        prev = 1

        for i in range(n - 1):
            temp = prev
            prev = lastNum + prev
            lastNum = temp
        return prev


        