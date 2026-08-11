class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l <= r:
            total_hours = 0
            m = l + ((r - l) // 2)
            for p in piles:
                total_hours += math.ceil(float(p) / m)
            if total_hours <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k

        