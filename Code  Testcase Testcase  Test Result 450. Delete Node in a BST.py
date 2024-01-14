class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Search for the node to remove
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.findMin(root.right)
            # Copy the inorder successor's content to this node
            root.val = temp.val
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, root.val)

        return root

    def findMin(self, node):
        while node.left:
            node = node.left
        return node
