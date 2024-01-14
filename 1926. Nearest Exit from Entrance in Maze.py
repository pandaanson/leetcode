from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        This function finds the shortest path from the entrance to the nearest exit in a maze.
        The maze is represented by a matrix with '.' as empty cells and '+' as walls.
        The entrance is not considered an exit. The function returns the number of steps
        to the nearest exit or -1 if no path exists.
        """
        queue = deque()
        maze[entrance[0]][entrance[1]] = "+"  # Mark the entrance as visited

        # Add adjacent cells to the queue if they are empty
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            x, y = entrance[0] + dx, entrance[1] + dy
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == ".":
                queue.append((x, y, 1))

        # BFS to find the nearest exit
        while queue:
            i, j, steps = queue.popleft()
            # Check if it's an exit
            if (i == 0 or j == 0 or i == len(maze) - 1 or j == len(maze[0]) - 1) and (i, j) != (entrance[0], entrance[1]):
                return steps

            # Explore adjacent cells
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == ".":
                    maze[x][y] = "+"  # Mark the cell as visited
                    queue.append((x, y, steps + 1))

        return -1  # No path to an exit
