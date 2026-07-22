class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s = 0
        l = len(matrix) - 1
        mat = 0
        while s <= l:
            med = (s + l) // 2
            
            if target < matrix[med][0]:
                l = med - 1
            elif target > matrix[med][len(matrix[med]) - 1]:
                s = med + 1
            else:
                mat = med
                break
        left = 0
        right = len(matrix[mat]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < matrix[mat][mid]:
                right = mid - 1
            elif target > matrix[mat][mid]:
                left = mid + 1
            else: 
                return True
        return False

            