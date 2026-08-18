class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_dict = {}

        for i, n in enumerate(nums):
            difference = target - n

            if difference in difference_dict:
                return [difference_dict[difference], i]
            difference_dict[n] = i
        return []
        