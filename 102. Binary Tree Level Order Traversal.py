class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Given the root of a binary tree, this function returns the level order traversal
        of its nodes' values, i.e., from left to right, level by level.
        """
        if not root:
            return []

        ans = []
        queue = deque([root])  # Queue for BFS

        while queue:
            level_size = len(queue)  # Determine the number of nodes at the current level
            level_nodes = []  # List to store the values of nodes at this level

            # Iterate through all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()  # Remove and get the front node from the queue
                level_nodes.append(node.val)  # Add the node's value to the level list

                # Add the left and right children of the node to the queue, if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Append the list of node values for this level to the answer
            ans.append(level_nodes)

        # Return the level order traversal result
        return ans
