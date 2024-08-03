#304 - range sum query 2D
#tags: prefix, matrix
#date: 8-2-24
#difficulty: medium
#time complexity: O(n^2)
#space complexity: O(n^2)
#-----------------------------------------------------------
#Given a 2D matrix matrix, handle multiple queries of the following type:

#Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#Implement the NumMatrix class:

#NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
#int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#You must design an algorithm where sumRegion works on O(1) time complexity.
#---------------------------------------------------------------
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])
        self.sumMatrix = [[0] * (COLUMNS + 1) for column in range(ROWS + 1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLUMNS):
                prefix = prefix + matrix[r][c]
                above = self.sumMatrix[r][c+1]
                #offset for extra zeros on either side
                self.sumMatrix[r+1][c+1] = prefix + above
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        above = self.sumMatrix[row1 -1][col2]
        left = self.sumMatrix[row2][col1-1]
        topleft = self.sumMatrix[row1-1][col1 -1]
        bottomright = self.sumMatrix[row2][col2]
        return bottomright - above - left + topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)