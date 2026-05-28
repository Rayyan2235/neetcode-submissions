class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for r in range(len(matrix)): 

            for c in range(len(matrix[0])): # Gets the length of the row to iterate it row times
                if matrix[r][c] == target:
                    return True
        return False
        