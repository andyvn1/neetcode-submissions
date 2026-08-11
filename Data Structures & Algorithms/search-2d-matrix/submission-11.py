class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        upper = 0
        bottom = ROWS - 1
        m = 0

        while upper <= bottom:
            m = (upper + bottom) // 2
            if target < matrix[m][0]:
                bottom = m - 1
            elif target > matrix[m][-1]:
                upper = m + 1
            else:
                break
        
        if upper > bottom:
            return False
        
        choosen_list = matrix[m]
        l = 0
        r = len(choosen_list) - 1

        while l <= r:
            m = (l + r) // 2
            if target < choosen_list[m]:
                r = m - 1
            elif target > choosen_list[m]:
                l = m + 1
            else:
                return True
        return False


            