class Solution:
    def climbStairs(self, n: int) -> int:
        last, prev = 1, 1

        for i in range(n - 1):
            temp = prev
            prev = prev + last
            last = temp
        return prev


        