class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        2x2 matrix therefore Min efficiency is O(n^2) can conclude thatdouble for   loop
        tracking duplicates therefore usage of set
        
        cases where immediately it fails:
            If there are dupes in row
                in col

        '''
        
        for row in range(len(board)):
            seen = set()
            for col in range(len(board[row])):
                val = board[row][col]
                if val == '.':
                    continue
                if val in seen:
                    return False
                seen.add(val)
        for col in range(len(board[row])):
            seen = set()
            for row in range(len(board)):
                val = board[row][col]
                if val =='.':
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for square in range(len(board)):
            seen = set()
            for row in range(3):
                for col in range(3):
                    row_s = (square//3) * 3 + row
                    col_s = (square % 3) * 3 + col
                    if board[row_s][col_s] == '.':
                        continue
                    if board[row_s][col_s] in seen:
                        return False
                    seen.add(board[row_s][col_s])
        return True
