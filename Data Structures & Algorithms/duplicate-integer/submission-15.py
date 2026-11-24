class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_d = set()
        for n in nums:
            if n in no_d:
                return True
            no_d.add(n)
        return False
        