class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashm = set()
        for n in nums:
            if n in hashm:
                return True
            hashm.add(n)
        return False
         