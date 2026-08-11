class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        mapa_hash = set()

        for n in nums:
            if n in mapa_hash:
                return True
            mapa_hash.add(n)
        return False

         