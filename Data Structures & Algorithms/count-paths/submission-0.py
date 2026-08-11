class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        bot = [1] * n
        for i in range(m - 1):
            newBot = [1] * n
            for j in range(n - 2, -1, -1):
                newBot[j] = newBot[j + 1] + bot[j]
            bot = newBot
        return bot[0] 
        