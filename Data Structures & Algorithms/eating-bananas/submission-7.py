class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        k = max(piles)
        end = k
        
        while start <= end:
            totalTime = 0
            m = (start + end)  // 2
            for p in piles:
                totalTime += math.ceil(p / m)
            if totalTime <= h:
                k = m
                end = m - 1
            elif totalTime > h:
                start = m + 1
        return k
        