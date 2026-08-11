class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicate = set()
        for n in nums:
            if n in no_duplicate:
                return True
            else:
                no_duplicate.add(n)
        return False
         