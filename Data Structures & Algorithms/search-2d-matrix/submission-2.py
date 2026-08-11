class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            left, right = matrix[i][0], matrix[i][len(matrix[i]) - 1]
            if target >= left and target <= right:
                inside_left, inside_right = 0, len(matrix[i]) - 1
                while inside_left <= inside_right:
                    m = inside_left + ((inside_right - inside_left) // 2)
                    if target > matrix[i][m]:
                        inside_left = m + 1
                    elif target < matrix[i][m]:
                        inside_right = m - 1
                    else:
                        return True
                return False
        return False

    



        