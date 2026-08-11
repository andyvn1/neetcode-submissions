class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        bot = [0] * n
        bot[n - 1] = 1

        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if c < n - 1:
                    bot[c] = bot[c] + bot[c + 1]
        return bot[0]
        