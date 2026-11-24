class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum_dict = {}
        for i, n in enumerate(nums):
            diference = target - n
            if diference in twoSum_dict:
                return [twoSum_dict[diference], i]
            twoSum_dict[n] = i
        return []