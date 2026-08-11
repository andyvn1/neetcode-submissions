class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones= 0
        internal_count = 0
        for i in range(len(nums)):
            if nums[i] == 1 and i < len(nums) - 1:
                internal_count += 1
            else:
                if nums[i] == 1:
                    internal_count += 1
                max_ones = max(max_ones, internal_count)
                internal_count = 0
        return max_ones


        