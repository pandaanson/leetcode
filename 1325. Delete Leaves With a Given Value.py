class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Recursively remove target leaves from left and right subtrees
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # If the current node becomes a leaf node with the target value, remove it
        if not root.left and not root.right and root.val == target:
            return None

        return root
