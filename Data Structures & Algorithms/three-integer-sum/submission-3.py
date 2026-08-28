class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output= []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            number = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum3 = nums[l] + nums[r] + number
                if sum3 < 0:
                    l += 1
                elif sum3 > 0:
                    r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return output
