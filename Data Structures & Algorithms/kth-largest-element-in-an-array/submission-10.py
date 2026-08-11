class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def dfs(l, r):

            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[r], nums[p] = nums[p], nums[r]

            if k < p:
                return dfs(l, p - 1)
            elif k > p:
                return dfs(p + 1, r)
            else:
                return nums[p]
        return dfs(0, len(nums) - 1)

        