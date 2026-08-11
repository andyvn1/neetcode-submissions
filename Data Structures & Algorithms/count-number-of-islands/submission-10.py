class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island = 0
        q = deque()
        visit = set()
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            q.append((r, c))
            visit.add((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in direction:
                    r, c= dr + row, dc + col
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit:
                        visit.add((r, c))
                        q.append((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    island += 1
        return island

                            




        