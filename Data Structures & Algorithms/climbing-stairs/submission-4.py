class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        before_last = 1
        for i in range(n - 1):
            temp = before_last 
            before_last = last + before_last
            last = temp
        return before_last
        