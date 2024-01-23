class Solution:
    def uniquePathsIII(self, grid):
        """
        Problem Statement:
        Given an m x n integer array 'grid', where 'grid[i][j]' could be:
          - 1 representing the starting square (exactly one starting square).
          - 2 representing the ending square (exactly one ending square).
          - 0 representing empty squares that can be walked over.
          - -1 representing obstacles that cannot be walked over.
        Return the number of 4-directional walks from the starting square to the ending square,
        such that every non-obstacle square is walked over exactly once.

        Solution Explanation:
        The solution uses depth-first search (DFS) to explore all possible paths from the starting
        square to the ending square, covering each non-obstacle square exactly once.
        """

        self.res = 0  # Counter for the number of valid paths
        m, n, empty = len(grid), len(grid[0]), 1  # Initialize dimensions and count of empty squares

        # Find the starting position and count empty squares
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = (i, j)  # Starting position
                elif grid[i][j] == 0:
                    empty += 1  # Count of empty squares

        def dfs(x, y, empty):
            # Check if the current position is valid
            if not (0 <= x < m and 0 <= y < n and grid[x][y] >= 0):
                return
            # Check if the ending square is reached
            if grid[x][y] == 2:
                self.res += empty == 0  # Increment result if all non-obstacle squares are covered
                return
            # Mark the current square as visited
            grid[x][y] = -2
            # Explore all 4 directions
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            # Backtrack: mark the square as unvisited
            grid[x][y] = 0

        # Start DFS from the starting square
        dfs(x, y, empty)
        return self.res

# Example usage
sol = Solution()
print(sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))  # Example input
