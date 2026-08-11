class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globMax = nums[0]
        currMax = 0

        for n in nums:
            currMax = max(currMax + n, n)
            globMax =  max(currMax, globMax)
        return globMax
        