class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        gmax = nums[0]
        curmax = 0

        for n in nums:
            curmax = max(curmax + n, n)
            gmax = max(curmax, gmax)
        
        return gmax
        