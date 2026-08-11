class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            firstStone = abs(heapq.heappop(stones))
            secondStone = abs(heapq.heappop(stones))
            if secondStone < firstStone:
                newStone = -1 * (firstStone - secondStone)
                heapq.heappush(stones, newStone)
        stones.append(0)
        return abs(stones[0])