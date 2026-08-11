class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        gmax = nums[0]
        cmax = 0

        for n in nums:
            cmax = max(cmax + n, n)
            gmax = max(gmax, cmax)

        return gmax       