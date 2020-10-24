class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # similar to binary search, but have to move the pointer by 1 (remove one row or one column each time). Start from lower left corner
        
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        n = len(matrix)
        m = len(matrix[0])
        
        x = n-1
        y = 0
        
        while x >= 0 and y < m:
            if  matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                x = x - 1
            else:
                y = y + 1

        return False
        
