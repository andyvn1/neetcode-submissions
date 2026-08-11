class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        grid = [[0] * (cols + 1) for i in range(rows + 1)]

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if text1[r] == text2[c]:
                    grid[r][c] = 1 + grid[r + 1][c + 1]
                else:
                    grid[r][c] = max(grid[r + 1][c], grid[r][c + 1])
        
        return grid[0][0]

        