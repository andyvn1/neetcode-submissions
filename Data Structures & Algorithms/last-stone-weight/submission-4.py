class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stonesX = abs(heapq.heappop(stones))
            stonesY = abs(heapq.heappop(stones))
            if stonesY < stonesX:
                newStone = -1 * (stonesX - stonesY)
                heapq.heappush(stones, newStone)
        
        stones.append(0)
        return abs(stones[0])
            

        
        