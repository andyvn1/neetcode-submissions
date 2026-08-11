class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differ_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in differ_map:
                return [differ_map[diff], i]
            differ_map[n] = i

            

        