class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for x in range(n):
            dp[0][x]=matrix[0][x]
        for y in range(1,m):
            for x in range(n):
                dp[y][x]=dp[y-1][x]
                if x>0:
                    dp[y][x]=min(dp[y-1][x-1],dp[y][x])
                if x<n-1:
                    dp[y][x]=min(dp[y-1][x+1],dp[y][x])
                dp[y][x]+=matrix[y][x]
        return min(dp[-1])
                    
