class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = set()
        for n in nums:
            hashMap.add(n)
        
        return len(hashMap) != len(nums)
        
        

         