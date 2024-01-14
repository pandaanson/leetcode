#Given a binary matrix grid of size m x n, where an island consists of contiguous cells with the value 1 connected either horizontally or vertically. The surrounding edges of the grid are all water (0's). The area of an island is defined as the count of cells with the value 1 that make up the island. Determine the largest area of any island present in the grid. If there are no islands, return 0.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0

        def rangeclearer(i, j):
            nonlocal temp  # Declare temp as nonlocal to modify it within this function
            grid[i][j] = 0
            temp += 1
            if i > 0 and grid[i - 1][j] == 1:
                rangeclearer(i - 1, j)
            if j > 0 and grid[i][j - 1] == 1:
                rangeclearer(i, j - 1)
            if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                rangeclearer(i, j + 1)
            if i < len(grid) - 1 and grid[i + 1][j] == 1:
                rangeclearer(i + 1, j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    temp = 0  # Initialize temp for each island
                    rangeclearer(i, j)
                    ans = max(temp, ans)

        return ans
                    
