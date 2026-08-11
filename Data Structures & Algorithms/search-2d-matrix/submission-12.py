class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        m = 0
        upper = 0
        lower = rows - 1

        while upper <= lower:
            m = (upper + lower) // 2
            if target < matrix[m][0]:
                lower = m - 1
            elif target > matrix[m][-1]:
                upper = m + 1
            else:
                break
        
        if upper > lower:
            return False
        
        choosenList = matrix[m]
        l, r = 0, len(choosenList)

        while l <= r:
            m = (l + r) // 2
            if target < choosenList[m]:
                r = m - 1
            elif target > choosenList[m]:
                l = m + 1
            else:
                return True
        return False


        

        