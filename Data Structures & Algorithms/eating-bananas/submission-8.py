class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate = max(piles)
        start, end = 1, rate

        while start <= end:
            total = 0
            m = (start + end) // 2
            for p in piles:
                total += math.ceil(float(p) / m)
            if total <= h:
                rate = m
                end = m - 1
            else:
                start = m + 1
        return rate
        