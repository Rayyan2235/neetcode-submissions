class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        '''
        we gotta traverse the matrix
        How do we calculate the midpoint?


        1  2  3  10
        4  5  6  11
        7  8  9  12
    '''

        
        row = len(matrix) # Counts from top to bottom
        col = len(matrix[0]) # looks at the first row and then counts how many in the first row
        l = 0
        r = row * col - 1

       
        while l <= r: 
            
            m = (r + l) // 2
            m_R = m // col # Finds the row index of the midpoint. This is done by finding how many times the position of 'm' goes into col to see which row you can find the midpoint.
            
            m_C = m % col

            if matrix[m_R][m_C] < target:
                l = m + 1
                
            elif matrix[m_R][m_C] > target:
                r = m - 1
            else:
                return True
        
        return False




        