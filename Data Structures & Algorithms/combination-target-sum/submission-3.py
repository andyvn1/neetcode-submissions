class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subsets, t):
            if t == target:
                res.append(subsets.copy())
                return
            if t > target or i >= len(nums):
                return
            
            subsets.append(nums[i])
            dfs(i, subsets, t + nums[i])

            subsets.pop()
            dfs(i + 1, subsets, t)
        dfs(0, [], 0)
        return res

            
        