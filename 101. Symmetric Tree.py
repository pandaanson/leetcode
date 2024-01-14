# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Given the root of a binary tree, this function checks if the tree is symmetric around its center.
        A tree is symmetric if the left subtree is a mirror reflection of the right subtree.
        """

        def is_mirror(left, right):
            """
            Helper function to check if two trees are mirror images of each other.
            """
            # Base case: if both nodes are None, they are symmetric.
            if not left and not right:
                return True
            # If one of the nodes is None or their values are not equal, the trees are not symmetric.
            if not left or not right or left.val != right.val:
                return False
            # Recursively check if the left subtree of one tree is a mirror image of the right subtree of the other tree.
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        # Start the check from the root of the tree.
        return is_mirror(root, root)

# Example usage
# Assume a valid TreeNode root is given
sol = Solution()
print(sol.isSymmetric(root))  # Output will be True if the tree is symmetric, otherwise False
