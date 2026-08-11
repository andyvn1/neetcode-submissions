class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapa = set()
        for n in nums:
            if n in mapa:
                return True
            mapa.add(n)
        return False
         