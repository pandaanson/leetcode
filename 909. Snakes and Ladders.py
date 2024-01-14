from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        Given a 2D board representing a snakes and ladders game, where each cell contains either -1 (no snake/ladder)
        or a positive integer indicating the destination cell of a snake or ladder. The objective is to find the minimum 
        number of moves required to reach the final cell from the first cell. Each move simulates the roll of a 6-sided die.

        Solution:
        First, flatten the board into a 1D array to represent the game as a linear sequence of cells.
        Then, use BFS to find the shortest path to the final cell.
        """
        n = len(board)
        # Flatten the board
        flattened = [0] * (n*n)
        idx = 0
        for r in range(n - 1, -1, -1):
            row = board[r][::1] if (n - 1 - r) % 2 == 0 else board[r][::-1]
            for val in row:
                flattened[idx] = val
                idx += 1

        # BFS to find the shortest path
        queue = deque([(1, 0)])  # Start from square 1 with 0 moves
        seen = set([1])
        while queue:
            curr, moves = queue.popleft()
            if curr == n*n:  # Reached the final cell
                return moves
            for next in range(curr + 1, min(curr + 6, n*n) + 1):
                dest = flattened[next - 1] if flattened[next - 1] != -1 else next
                if dest not in seen:
                    seen.add(dest)
                    queue.append((dest, moves + 1))
        return -1  # Not possible to reach the final cell
