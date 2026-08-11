class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return None
        mapa_hash = {}
        
        for i, n in enumerate(nums):
            difference = target - n
            if difference in mapa_hash:
                return [mapa_hash[difference], i]  
            mapa_hash[n] = i
        
            
        