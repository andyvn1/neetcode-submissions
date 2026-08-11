class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Row, Col = len(matrix), len(matrix[0])
        top, bottom = 0, Row - 1

        while top <= bottom:
            m = top + ((bottom - top) // 2)

            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bottom = m - 1
            else:
                break
        if not top <= bottom:
            return False
        
        choosen_list = matrix[m]
        l, r = 0, len(choosen_list)
        while l <= r:
            m = l + ((r - l) // 2)

            if target > choosen_list[m]:
                l = m + 1
            elif target < choosen_list[m]:
                r = m - 1
            else:
                return True
        return False
        