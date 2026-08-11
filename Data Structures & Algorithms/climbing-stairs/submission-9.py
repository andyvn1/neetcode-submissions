class Solution:
    def climbStairs(self, n: int) -> int:
        lastStair = 1
        beforeLast = 1
        for i in range(n-1):
            temp = beforeLast
            beforeLast = lastStair + beforeLast
            lastStair = temp
        return beforeLast
        