class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        tri = [[1]*i for i in range(1, numRows+1)] #build data structure

        for row in range(2, numRows):
            for col in range(1, row):
                tri[row][col] = tri[row-1][col-1] + tri[row-1][col]
        
        return tri