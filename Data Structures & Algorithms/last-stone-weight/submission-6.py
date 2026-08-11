class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stoneY = abs(heapq.heappop(stones))
            stoneX = abs(heapq.heappop(stones))
            if stoneX < stoneY:
                heapq.heappush(stones, -1 * (stoneY - stoneX))
        stones.append(0)
        return abs(stones[0])
        
        