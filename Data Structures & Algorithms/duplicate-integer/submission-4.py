class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates_allowed = set()
        for n in nums:
            if n in no_duplicates_allowed:
                return True
            no_duplicates_allowed.add(n)
        return False

