class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        perimeter = 0

        def is_water_or_outside(x, y):
            return x < 0 or y < 0 or x >= cols or y >= rows or grid[y][x] == 0

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 1:
                    stack = [(x, y)]
                    while stack:
                        cx, cy = stack.pop()
                        if (cx, cy) in visited:
                            continue
                        visited.add((cx, cy))

                        # Check each direction and count the perimeter
                        for dx, dy in direction:
                            nx, ny = cx + dx, cy + dy
                            if is_water_or_outside(nx, ny):
                                perimeter += 1
                            elif (nx, ny) not in visited:
                                stack.append((nx, ny))

                    # Once the island is fully explored, return the perimeter
                    return perimeter

        return perimeter
