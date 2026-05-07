class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def row(i):
            return board[i]
        
        def col(i):
            array = []
            for j in range(9):
                array.append(board[j][i])
            return array
        
        def square(i, j):
            array = []
            for x in range(3):
                for y in range(3):
                    array.append(board[i*3 + x][j*3 + y])
            return array
        
        def hasDuplicateNum(array):
            nums = [n for n in array if n.isdigit()]
            return len(nums) != len(set(nums))
        
        for i in range(9):
            if hasDuplicateNum(row(i)) or hasDuplicateNum(col(i)) \
                    or hasDuplicateNum(square(i // 3, i % 3)):
                return False
        
        return True
