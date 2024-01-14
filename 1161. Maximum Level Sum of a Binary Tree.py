from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return the smallest level number where the sum of
        all the node values at that level is maximal.
        """
        if not root:
            return 0

        max_sum = float('-inf')
        max_level = 0
        level = 1
        queue = deque([root])

        while queue:
            level_sum = 0
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            level += 1

        return max_level
