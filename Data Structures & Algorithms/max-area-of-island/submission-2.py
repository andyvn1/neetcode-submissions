class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r, c) in visit):
                return 0

            visit.add((r, c))
            return (1 + bfs(r + 1, c) +
                        bfs(r - 1, c) +
                        bfs(r, c + 1) +
                        bfs(r, c - 1) )

        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, bfs(r, c))
        return area