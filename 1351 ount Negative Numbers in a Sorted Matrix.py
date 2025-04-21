import numpy as np
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        n = 0
        m = 0
        arr = np.grid()
        print("grid: ", grid)
        print("arr: ", arr)
        while m < len(grid):
            while n < len(grid[0]):
                if grid[m[n]] < 0:
                    count += 1
        return count