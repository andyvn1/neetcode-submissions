class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        stack = []

        for x, y in points:
            dis = x**2 + y**2
            stack.append([dis, x, y])
        
        heapq.heapify(stack)
        res = []

        while k > 0:
            dis, x, y = heapq.heappop(stack)
            res.append([x, y])
            k -= 1

        return res 
        