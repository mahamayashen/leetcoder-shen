class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = []
        if target < matrix[0][0]: return False
        
        i = 0
        while i <= len(matrix) - 1:
            if target == matrix[i][0]:
                return True
            elif target < matrix[i][0]:
                index.append(i-1)
                break
            else:
                i += 1
                
        if len(index) == 0:
            index.append(len(matrix) - 1)
        
        j = len(matrix[0]) - 1
        if target > matrix[index[0]][j]: return False

        while j >= 0:
            if target == matrix[index[0]][j]:
                return True
            elif target < matrix[index[0]][j]:
                j -= 1
            else:
                return False