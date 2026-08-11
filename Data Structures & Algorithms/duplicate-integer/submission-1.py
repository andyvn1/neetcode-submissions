class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = set()
        for n in nums:
            if n in hashMap:
                return True
            hashMap.add(n)
        return False
                
         