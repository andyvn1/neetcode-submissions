class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            yStone = abs(heapq.heappop(stones))
            xStone = abs(heapq.heappop(stones))
            if xStone < yStone:
                newStone = yStone - xStone
                heapq.heappush(stones, -1 * newStone)
        stones.append(0)
        return abs(stones[0]) 
        