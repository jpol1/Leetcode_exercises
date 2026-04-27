class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        
        visited = [[False]*n for _ in range(m)]

        streets = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        opposite = {
            (0, 1): (0, -1),
            (0, -1): (0, 1),
            (1, 0): (-1, 0),
            (-1, 0): (1, 0)
        }

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return True

            visited[r][c] = True
            for dr, dc in streets[grid[r][c]]:
                nr = dr + r
                nc = dc + c

                if nr < 0 or nr>=m or nc<0 or nc>=n:
                    continue
                
                if visited[nr][nc]:
                    continue
                
                if opposite[(dr, dc)] not in streets[grid[nr][nc]]:
                    continue

                if dfs(nr, nc):
                    return True
            return False

        return dfs(0,0)