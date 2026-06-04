def replace_0_1(arr, visited):
    for idx in visited:
        row, col = idx
        arr[row][col] = 'X'

def dfs(arr, idx):
    n = len(arr)
    m = len(arr[0])
    touches_border = True if (idx[0] == 0 or idx[1] == 0 or idx[0] == n-1 or idx[1] == m-1) else False
        
        
    visited = {idx}
    stack = [idx]
    
    while stack:
        row,col = stack.pop()
        
        np = [
            (row+1, col),
            (row-1, col),
            (row, col+1),
            (row, col-1)
            ]
        
        for nr, nc in np:
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            
            if arr[nr][nc] != 'O':
                continue
            
            if nr == 0 or nc == 0 or nr == n-1 or nc == m-1:
                touches_border = True
            
            if (nr, nc) not in visited:
                visited.add( (nr,nc) )
                stack.append( (nr,nc) )
    
    if not touches_border:
        replace_0_1(arr, visited)
    return visited

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        n = len(board)
        m = len(board[0])
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'O' and (row, col) not in visited:
                    visited.update(dfs(board, (row, col)))