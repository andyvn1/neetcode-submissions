class Solution:
    def climbStairs(self, n: int) -> int:
        last_step = 1
        before_step = 1
        while n > 1:
            nextStep = last_step + before_step
            last_step = before_step
            before_step = nextStep
            n -= 1
        return before_step
            

        