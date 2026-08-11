class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)  - 1
        while top <= bottom:
            m = (top + bottom) // 2
            if  target < matrix[m][0]:
                bottom = m - 1
            elif target > matrix[m][-1]:
                top =  m + 1
            else:
                break

        if top > bottom:
            return False

        choosen = matrix[m]
        l, r = 0, len(choosen) -1
        while l <= r:
            p = (l + r) // 2
            if target < choosen[p]:
                r = p - 1
            elif target > choosen[p]:
                l = p + 1
            else:
                return True
        return False



        