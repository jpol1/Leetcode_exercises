class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        for r in range(rows):
            for c in range(cols):
                if c > r:
                    matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]
        
        for r in range(rows):
            for c in range(cols//2):
                matrix[r][c], matrix[r][cols-1-c] = matrix[r][cols-1-c], matrix[r][c]

