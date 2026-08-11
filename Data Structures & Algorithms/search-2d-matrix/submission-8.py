class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix)
        top, bottom = 0, col - 1
        while top <= bottom:
            m = (top + bottom) // 2
            if target < matrix[m][0]:
                bottom = m - 1
            elif target > matrix[m][-1]:
                top = m + 1
            else:
                break

        choosen = matrix[m]
        l, r = 0, len(choosen) - 1
        while l <= r:
            m = (l + r)  // 2
            if target < choosen[m]:
                r = m - 1
            elif target > choosen[m]:
                l = m + 1
            else:
                return True
        return False
         
        