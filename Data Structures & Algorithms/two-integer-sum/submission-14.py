class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_hash = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in difference_hash:
                return [difference_hash[difference], i]
            difference_hash[n] = i
        return []


