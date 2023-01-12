class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for row in range(9):
            dic = {}
            for col in range(9):
                if board[row][col] != '.':
                    num = int(board[row][col])
                    dic[num] = dic.get(num, 0) + 1
                    if dic[num] > 1:
                        return False

        # check col
        for col in range(9):
            dic = {}
            for row in range(9):
                if board[row][col] != '.':
                    num = int(board[row][col])
                    dic[num] = dic.get(num, 0) + 1
                    if dic[num] > 1:
                        return False

        # check sub-box
        row_new = 0
        col_new = 0
        while row_new < 9:
            col_new = 0
            while col_new < 9:
                dic = {}
                for row in range(row_new, row_new + 3):
                    for col in range(col_new, col_new + 3):
                        if board[row][col] != '.':
                            num = int(board[row][col])
                            dic[num] = dic.get(num, 0) + 1
                            if dic[num] > 1:
                                return False
                col_new += 3
            row_new += 3

        return True