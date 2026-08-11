class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        before = 1
        for i in range(n - 1):
            temp = before
            before = last + before
            last = temp
        return before
            
            

        