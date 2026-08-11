class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
                
        rows, cols = len(grid), len(grid[0])
        island = 0
        visit = set()
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        def dfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            while q:
                r, c = q.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in visit:
                        q.append((row, col))
                        visit.add((row, col))
                   


        for r in range(rows):
            for c in range(cols):
                if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    island += 1
        return island




        