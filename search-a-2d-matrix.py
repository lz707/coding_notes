class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # use binary search. Twist is to find corresponding matrix item from midpint. x = mid // num_columns, y = mid % num_columns
    
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        n = len(matrix)
        m = len(matrix[0])

        start = 0
        end = n*m -1
        
        while start < end -1:
            mid = start + (end - start)/2
            x = int(mid//m)
            y = int(mid%m)
            
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid
            
        if matrix[int(start//m)][int(start%m)] == target:
            return True
        elif matrix[int(end//m)][int(end%m)] == target:
            return True
        else:
            return False
