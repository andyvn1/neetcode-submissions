class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stack = []
        i = 0
        while i < len(nums):
            for j in range(len(nums)):
                if i != j:
                    num = nums[i] + nums[j]
                    if num == target:
                        stack.append([i, j])
                        break
            i += 1
        return stack[0]


        