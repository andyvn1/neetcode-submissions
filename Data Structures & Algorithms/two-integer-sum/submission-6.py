class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapa = {}
        for i, n in enumerate(nums):
            diss = target - n
            if diss in mapa:
                return [mapa[diss], i]
            mapa[n] = i
        
        