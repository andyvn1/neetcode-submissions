class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapa = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapa:
                return [mapa[diff], i]
            else:
                mapa[n] = i
     
            
        