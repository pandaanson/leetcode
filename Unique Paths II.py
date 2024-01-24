class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0  # No paths if the start or end is an obstacle

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1  # Starting point

        for y in range(m):
            for x in range(n):
                if obstacleGrid[y][x] == 1:
                    dp[y][x] = 0  # No paths through an obstacle
                else:
                    if x > 0:
                        dp[y][x] += dp[y][x-1]  # Paths from the left
                    if y > 0:
                        dp[y][x] += dp[y-1][x]  # Paths from the top

        return dp[m-1][n-1]  # Number of paths to the bottom-right corner

# Example usage
sol = Solution()
print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))  # Output: 2
