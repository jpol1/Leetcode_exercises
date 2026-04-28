class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        steps = 0

        flatted_grid = [num for row in grid for num in row]

        first_modulo = flatted_grid[0] % x
        for num in flatted_grid:
            if num % x != first_modulo:
                return -1
        
        flatted_grid.sort()

        minimize_number = flatted_grid[len(flatted_grid) // 2]

        for num in flatted_grid:
            if num == minimize_number:
                continue
            else:
                steps += abs(num-minimize_number) / x
        
        return steps