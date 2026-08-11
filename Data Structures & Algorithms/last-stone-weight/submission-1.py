class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            firstNum = abs(heapq.heappop(stones))
            secondNum = abs(heapq.heappop(stones))

            if firstNum > secondNum:
                heapq.heappush(stones, -1 * (firstNum - secondNum))
        stones.append(0)
        return abs(stones[0])
        