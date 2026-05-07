class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)]
        grid[0][0] = 1
        for row in range(m):
            for col in range(n):
                if (row == 0):
                    continue
                elif (col == 0):
                    continue
                else:
                    grid[row][col] = grid[row-1][col] + grid[row][col-1]
        return grid[m-1][n-1]