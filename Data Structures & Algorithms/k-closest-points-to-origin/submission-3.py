class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []

        for x, y in points:
            d = x**2 + y**2
            ans.append([d, x, y])

        heapq.heapify(ans)

        res = []
        while k > 0:
            d, x, y = heapq.heappop(ans)
            res.append([x, y])
            k -= 1
        return res