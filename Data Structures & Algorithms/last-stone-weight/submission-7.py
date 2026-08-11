class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            stoneX = abs(heapq.heappop(stones))
            stoneY = abs(heapq.heappop(stones))
            if stoneX > stoneY:
                heapq.heappush(stones, -1 * (stoneX - stoneY))
        stones.append(0)
        return abs(stones[0])

