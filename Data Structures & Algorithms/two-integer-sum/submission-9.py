class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            diference = target - nums[i]
            if diference in dic:
                return [dic[diference], i]
            dic[nums[i]] = i



        