from collections import deque

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        """
        Rephrased Question:
        Given a list of bombs, each represented as [xi, yi, ri] where xi and yi are the coordinates and ri is the radius,
        determine the maximum number of bombs that can be detonated. Detonating one bomb can trigger others within its radius.
        The task is to find the maximum number of bombs that can be detonated by initially detonating a single bomb.

        Solution:
        Use BFS to explore bomb detonations and DP to store the results of previous computations.
        """
        def in_range(bomb1, bomb2):
            # Function to check if bomb2 is within the range of bomb1
            x1, y1, r1 = bomb1
            x2, y2, _ = bomb2
            return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2

        n = len(bombs)
        dp = [-1] * n  # DP array to store the number of bombs each bomb can detonate
        max_detonations = 0

        def bfs(start):
            # BFS function to calculate the number of bombs detonated starting from 'start'
            if dp[start] != -1:  # Return stored value if already computed
                return dp[start]
            queue = deque([start])
            visited = set([start])
            while queue:
                current = queue.popleft()
                for j in range(n):
                    if j not in visited and in_range(bombs[current], bombs[j]):
                        visited.add(j)
                        queue.append(j)
            dp[start] = len(visited)  # Store the result in the DP array
            return dp[start]

        for i in range(n):
            # Update the maximum number of detonations for each bomb
            max_detonations = max(max_detonations, bfs(i))

        return max_detonations

# Example usage
bombs = [[2, 1, 3], [6, 1, 4]]
sol = Solution()
print(sol.maximumDetonation(bombs))  # Output will be the maximum number of bombs detonated
