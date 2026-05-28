class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Pattern: Binary search
        Want to iterate over the matrix using row and columns
        then can use binary saearch logic
        
        Issues I faced
        How do I get the midpoint? Use  row * col
        How do I access the 2d array, for instance finding the midpoint of the 2d array
            A) First we need to convert m which is a 1D index to a 2D index since we are dealing w a 2D array
            How do we find 'm' as a 2D plot, what is its row and col 
            The key insight: You're essentially asking "how many complete rows have I filled?" (division) 
            and "where in the current row am I?" (modulo).
            
            Why does division work: Because division means how many times x has filled up y 
            Why does mODULO work: Because it means how many times where it remains

        '''

        row = len(matrix)
        col = len(matrix[0])

        l = 0
        r = row * col - 1 # Gives the length of the whole 2d array

        while l <= r:
            m = (r + l) // 2
            row_index = m // col #Logic: how many times has the midpoint passed 'col' (a row)
            col_index = m % col  #Issue was here, I wrote col_index = m % row #Logic:  Where in the row it remains
            if matrix[row_index][col_index] < target:
                l = m + 1
            elif matrix[row_index][col_index] > target:    
                r = m - 1
            else:
                return True
        return False            






        

        
        