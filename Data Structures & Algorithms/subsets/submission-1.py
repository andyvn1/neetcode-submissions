class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []

        def helper(i):
            if i >= len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            helper(i + 1)
            
            sub.pop()
            helper(i + 1)
        helper(0)
        return res
            
        