class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diference_dict = {}

        for i, n in enumerate(nums):
            diference = target - n
            if diference in diference_dict:
                return [diference_dict[diference], i]
            diference_dict[n] = i
        return []
        