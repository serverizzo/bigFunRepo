import math

class Solution:
    
    completed = False
    # board
    
    def checkBox(self, row, col, val):
        rowThird = math.floor(row/3)
        colThird = math.floor(col/3)
        rowThird *= 3
        colThird *= 3
        for i in range(3):
            for j in range(3):
                if (rowThird + i == row) and (colThird + j == col):
                    continue
                if self.board[rowThird + i][colThird + j] == val:
                    return False
        return True

    def checkRow(self, row, col, val):
        for i in range(9):
            if i == col:
                continue
            else:
                if self.board[row][i] == val:
                    return False
        return True

    def checkCol(self, row, col, val):
        for i in range(9):
            if i == row:
                continue;
            else:
                if self.board[i][col] == val:
                    return False
        return True


    def helper(self, row, col):
        if col > 8:
            col = 0
            row += 1
        if row > 8:
            # print(self.board)
            self.completed = True
            return
        if self.board[row][col] != '.':
            self.helper(row,col + 1)                 
        else:
            for i in range(1,10):
                i = str(i)
                if self.checkBox(row, col, i) and self.checkRow(row, col, i) and self.checkCol(row, col, i) and not self.completed:
                    self.board[row][col] = i
                    self.helper(row, col + 1)
                    if self.completed is False:
                        self.board[row][col] = '.'
                        
                        
    def solveSudoku(self, board) -> None:
        self.board = board
        self.helper(0,0)
    """
    Do not return anything, modify board in-place instead.
    """
    
    def prettyPrint(self, input):
      rCount = 0
      cCount = 0
      for row in input:
        for ele in row:
          print(ele, end = " ")
          cCount += 1
          if cCount % 3 == 0:
            print(" ", end = "")
        print()
        rCount += 1
        if rCount % 3 == 0:
          print()
            
            
            

input = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
  ]

s = Solution()
s.solveSudoku(input)
s.prettyPrint(input)