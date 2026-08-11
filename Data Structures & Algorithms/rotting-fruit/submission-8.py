class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time, fresh = 0, 0
        rotten = deque()
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))

        while rotten and fresh > 0:
            for i in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        rotten.append((row, col))
            time += 1
        return time if fresh == 0 else -1



            
        