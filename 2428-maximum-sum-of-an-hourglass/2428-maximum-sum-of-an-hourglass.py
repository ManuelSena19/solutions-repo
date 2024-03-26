class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        max_sum = float('-inf')
        for i in range(m - 2):
            for j in range(n - 2):
                hourglass_sum = sum(grid[i][j:j+3]) + grid[i+1][j+1] + sum(grid[i+2][j:j+3])
                max_sum = max(max_sum, hourglass_sum)
        return max_sum