def dfs(arr: List[List[int]], idx: tuple):
    n = len(arr)
    m = len(arr[0])
    stack = [idx]
    
    arr[idx[0]][idx[1]] = "0"
    
    while stack:
        row, col = stack.pop()
        if (row + 1 < n and arr[row+1][col] == "1"):
            stack.append( (row+1, col) )
            arr[row+1][col] = "0"
        
        if (row - 1 >= 0 and arr[row-1][col] == "1"):
            stack.append( (row-1, col) )
            arr[row-1][col] = "0"
            
        if (col + 1 < m and arr[row][col+1] == "1"):
            stack.append( (row, col+1) )
            arr[row][col+1] = "0"
        
        if (col - 1 >= 0 and arr[row][col-1] == "1"):
            stack.append( (row, col-1) )
            arr[row][col-1] = "0"

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = 0, 0
        counter = 0
        n = len(grid)
        m = len(grid[0])
        
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1":
                    dfs(grid, (row, col) )
                    counter += 1
            
        return counter