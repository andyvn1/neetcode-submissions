class Solution:
    def climbStairs(self, n: int) -> int:
        lastStep = 1
        beforeLast = 1
        for i in range(n - 1):
            temp = beforeLast
            beforeLast = lastStep + beforeLast
            lastStep = temp
        return beforeLast
        
        