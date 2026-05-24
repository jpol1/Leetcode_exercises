class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ships = 0
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == "X":
                    flag = True
                    prev_column = column - 1
                    prev_row = row - 1
                    if prev_column >= 0 :
                        if board[row][prev_column] == "X":
                            flag = False
                    if prev_row >= 0 :
                        if board[prev_row][column] == "X":
                            flag = False
                    
                    if flag:
                        ships+=1
        return ships