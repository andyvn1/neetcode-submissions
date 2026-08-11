class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, n in enumerate(nums):
            diference = target - n
            if diference in dictionary:
                return [dictionary[diference], i]
            else:
                dictionary[n] = i
        return []

