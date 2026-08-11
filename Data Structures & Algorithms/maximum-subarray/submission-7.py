class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Gmax = nums[0]
        cmax = 0

        for n in nums:
            cmax = max(cmax + n, n)
            Gmax = max(cmax, Gmax)
        
        return Gmax
        