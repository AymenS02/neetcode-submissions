class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row = []
            for a in range(9):
                if board[i][a] in row and board[i][a] != ".":
                    return False
                row.append(board[i][a])

            col = []
            for a in range(9):
                if board[a][i] in col and board[a][i] != ".":
                    return False
                col.append(board[a][i])

        # Boxes: OUTSIDE the for-loop
        a = 0
        while a != 9:              # 0, 3, 6
            b = 0
            while b != 9:          # 0, 3, 6
                box = []           # fresh list for EACH box

                r = 0
                while r != 3:      # row offset inside box
                    c = 0
                    while c != 3:  # col offset inside box
                        val = board[a + r][b + c]
                        if val != "." and val in box:
                            return False
                        box.append(val)
                        c += 1
                    r += 1

                b += 3
            a += 3

        return True