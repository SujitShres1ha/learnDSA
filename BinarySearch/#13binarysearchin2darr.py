class Solution():
    def searchMatrix(self, matrix, target):
        rowStart = 0
        rowEnd = len(matrix) - 1
        colMid = len(matrix[0])//2
        cols = len(matrix[0]) - 1
        
        while (rowStart < rowEnd - 1):
            rowMid = (rowStart + rowEnd) // 2
            if (target == matrix(rowMid,colMid)):
                return [rowMid, colMid]
            if (target > matrix(rowMid,colMid)):
                rowStart = rowMid
            else:
                rowEnd = rowMid
        
        if (target == matrix[rowStart][colMid]):
            return [rowStart,colMid]
        if (target == matrix[rowStart+1][colMid]):
            return [rowStart,colMid]
        if (target < matrix[rowStart][colMid]):
            self.BinarySearch(matrix, 0, colMid - 1, rowStart, target)
        if (target > matrix[rowStart][colMid] and target <= matrix[rowStart][cols]):
            self.BinarySearch(matrix, colMid + 1, len(matrix[0]), rowStart, target)
        
        if (target < matrix[rowStart+1][colMid]):
            self.BinarySearch(matrix, 0, colMid - 1, rowStart+1, target)
        if (target > matrix[rowStart+1][colMid] and target <= matrix[rowStart+1][cols]):
            self.BinarySearch(matrix, colMid + 1, len(matrix[0]), rowStart+1 , target)





    def BinarySearch(self, matrix, colStart, colEnd, row, target):
        while (colStart <= colEnd):
            colMid = (colStart + colEnd) // 2
            if (target == matrix[row][colMid]):
                return [row, colMid]
            if (target > matrix[row][colMid]):
                colStart = colMid + 1
            else:
                colEnd = colMid - 1
        return [-1,-1]
            
