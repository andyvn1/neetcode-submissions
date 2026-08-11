class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0] * (len(text1) + 1) for i in range(len(text2) + 1)]
        
        for r in reversed(range(len(text2))):
            for c in reversed(range(len(text1))):
                if text1[c] == text2[r]:
                    grid[r][c] = 1 + grid[r + 1][c + 1] 
                else:
                    grid[r][c] = max(grid[r + 1][c], grid[r][c + 1])
        return grid[0][0]