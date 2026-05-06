class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        

        n_cols = len(boxGrid)
        n_rows = len(boxGrid[0])

        for row in range(n_cols):
            fast_p = n_rows-1
            slow_p = n_rows-1

            while(fast_p >= 0 and slow_p >= 0):
                if boxGrid[row][fast_p] == "*":
                    fast_p -= 1
                    slow_p = fast_p

                elif boxGrid[row][slow_p] != ".":
                    slow_p -= 1
                    fast_p = min(fast_p, slow_p)

                elif boxGrid[row][fast_p] == "#":
                    boxGrid[row][fast_p], boxGrid[row][slow_p] = boxGrid[row][slow_p], boxGrid[row][fast_p]
                    slow_p -= 1
                    fast_p -= 1

                else:
                    fast_p -= 1
                

        res = [[""] * n_cols for _ in range(n_rows)]

        for row in range(n_rows):
            for col in range(n_cols):
                res[row][col] = boxGrid[n_cols-col-1][row]

        return res