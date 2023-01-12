class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = []
        i = 0
        j = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                flat.append(mat[i][j])
        
        i = 0
        new_mat = []
        if r * c == len(flat):
            while i < len(flat):
                new_mat.append(flat[i:i+c])
                i += c
            return new_mat      
        else:
            return mat