class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, b = 0, len(matrix) - 1
        m = 0

        while u <= b:
            m = (u + b) // 2
            if target < matrix[m][0]:
                b = m - 1
            elif target > matrix[m][-1]:
                u = m + 1
            else:
                break
        
        if u > b:
            return False
        
        choosenList = matrix[m]
        l, r = 0, len(choosenList) - 1
        
        while l <= r:
            n = (l + r) // 2
            if target < choosenList[n]:
                r = n - 1
            elif target > choosenList[n]:
                l = n + 1
            else:
                return True
        
        return False
        