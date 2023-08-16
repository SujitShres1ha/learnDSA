class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = 0
        col = len(matrix[row])-1
        while (row <= len(matrix)-1 and col >= 0):
            if (target < matrix[row][col]):
                col -= 1
            elif (target > matrix[row][col]):
                row += 1
            else:
                return True
        return False