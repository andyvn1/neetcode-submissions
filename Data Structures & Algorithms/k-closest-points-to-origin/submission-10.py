class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        wdis = []
        for x, y in points:
            dis = x**2 + y**2
            wdis.append([dis, x, y])
        heapq.heapify(wdis)

        res = []
        while k > 0:
            dis, x, y = heapq.heappop(wdis)
            res.append([x, y])
            k -= 1
        return res
            
        