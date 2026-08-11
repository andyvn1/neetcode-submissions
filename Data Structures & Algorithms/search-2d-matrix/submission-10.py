class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        top, bot = 0, rows - 1
        m = 0
        while top <= bot:
            m = (top + bot) // 2
            if target < matrix[m][0]:
                bot = m - 1
            elif target > matrix[m][-1]:
                top = m + 1
            else:
                break

        if top > bot:
            return False
        
        choosenlist = matrix[m]
        l, r = 0, len(choosenlist) - 1
        while l <= r:
            m = (l + r) // 2
            if target < choosenlist[m]:
                r = r - 1
            elif target > choosenlist[m]:
                l = m + 1
            else:
                return True
        return False