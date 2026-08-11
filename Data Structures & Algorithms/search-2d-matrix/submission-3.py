class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Col = len(matrix), len(matrix[0])
        top, bot = 0, Rows - 1

        while top <= bot:
            m = top + ((bot - top) // 2)

            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bot = m - 1
            else:
                break
        
        if not top <= bot:
            return False

        chosen_list = matrix[m]
        l, r = 0, Col - 1
        while l <= r:
            m = l + ((r - l) // 2)

            if target > chosen_list[m]:
                l = m + 1
            elif target < chosen_list[m]:
                r = m - 1
            else:
                return True
        return False
        