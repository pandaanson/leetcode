from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        rotten_queue = deque()

        # Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten_queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        minutes_passed = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Process the rotten oranges level by level
        while rotten_queue and fresh_count > 0:
            minutes_passed += 1
            for _ in range(len(rotten_queue)):
                x, y = rotten_queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        rotten_queue.append((nx, ny))

        return minutes_passed if fresh_count == 0 else -1
