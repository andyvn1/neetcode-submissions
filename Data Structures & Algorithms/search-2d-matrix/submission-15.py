class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_cols, right_cols = 0, len(matrix) - 1

        while left_cols <= right_cols:
            mid = left_cols + (right_cols - left_cols) // 2

            if target < matrix[mid][0]:
                right_cols = mid - 1
            elif target > matrix[mid][-1]:
                left_cols = mid + 1
            else:
                break
        
        row = matrix[mid]
        l, r = 0, len(row) - 1
        while l <= r:
            mid = l + (r - l) // 2

            if target < row[mid]:
                r = mid - 1
            elif target > row[mid]:
                l = mid + 1
            else:
                return True
        return False

        