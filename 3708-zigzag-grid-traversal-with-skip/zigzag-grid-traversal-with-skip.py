class Solution(object):
    def zigzagTraversal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        result = []
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            if i % 2 == 0:
                for j in range(n):
                    if (i + j) % 2 == 0:
                        result.append(grid[i][j])
            else:
                for j in range(n - 1, -1, -1):
                    if (i + j) % 2 == 0:
                        result.append(grid[i][j])
                        
        return result