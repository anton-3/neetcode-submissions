class Solution:
    def matrixGet(self, matrix: List[List[int]], index: int) -> int:
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of columns
        row = index // n
        column = index % n
        return matrix[row][column]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # initialize left and right pointers to the first and last indices of array
        # while left < right, find the index that's the midpoint between left and right
        # if it's less, set left to midpoint+1
        # if the number there is greater than the target, set right to midpoint-1,
        left = 0
        right = m * n - 1
        while left < right:
            mid = (left + right) // 2
            midNum = self.matrixGet(matrix, mid)
            if midNum < target:
                left = mid + 1
            elif midNum > target:
                right = mid - 1
            else:
                return True
        if self.matrixGet(matrix, left) == target:
            return True
        return False