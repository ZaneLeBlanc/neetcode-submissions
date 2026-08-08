class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if self.isRowValid(board, i) == False:
                return False
        
        for i in range(9):
            if self.isColumnValid(board, i) == False:
                return False

        for i in range(9):
            if self.isBoxValid(board, i) == False:
                return False
        return True

        
    def isRowValid(self, board, rowNum):
        nums = {0}
        for i in range(9):
            val = board[rowNum][i]
            if val != '.':
                if val in nums:
                    return False
                else:
                    nums.add(val)
        return True

            

    def isColumnValid(self, board, colNum):
        nums = {0}
        for i in range(9):
            val = board[i][colNum]
            if val != '.':
                if val in nums:
                    return False
                else:
                    nums.add(val)
        return True

    def isBoxValid(self, board, boxNum):
    # 0, 1, 2
    # 3, 4, 5
    # 6, 7, 8
        offsetX = 0
        offsetY = 0
        match(boxNum):
            case 0:
                offsetX = 0
                offsetY = 0
            case 1:
                offsetX = 3
                offsetY = 0
            case 2:
                offsetX = 6
                offsetY = 0

            case 3:
                offsetX = 0
                offsetY = 3
            case 4:
                offsetX = 3
                offsetY = 3
            case 5:
                offsetX = 6
                offsetY = 3

            case 6:
                offsetX = 0
                offsetY = 6
            case 7:
                offsetX = 3
                offsetY = 6
            case 8:
                offsetX = 6
                offsetY = 6

        #check the box
        nums = {0}

        for i in range(offsetX, offsetX+3):
            for y in range(offsetY, offsetY+3):
                val = board[y][i]
                print(val)
                if val != '.':
                    if val in nums:
                        return False
                    else:
                        nums.add(val)
            print('')
        return True
