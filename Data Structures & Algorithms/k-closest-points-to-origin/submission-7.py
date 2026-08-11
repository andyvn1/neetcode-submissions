class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        storage = []
        for x, y in points:
            distance = x**2 + y**2
            storage.append([distance, x, y])
        heapq.heapify(storage)

        res = []
        while k > 0:
            dis, x, y = heapq.heappop(storage)
            res.append([x, y])
            k -= 1
        return res


        