# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, find the length of the longest ZigZag path in the tree.
        A ZigZag path is defined as a path where the direction changes between right and left at each step.
        The length of a ZigZag path is the number of nodes in the path minus one.

        Solution with Inline Explanation:
        """

        def helper(node):
            """
            Helper function to compute the longest ZigZag path starting from 'node'.
            It returns a list [left_len, right_len, max_len] where:
            - left_len is the length of the longest ZigZag path starting from 'node' and going left first.
            - right_len is the length of the longest ZigZag path starting from 'node' and going right first.
            - max_len is the maximum length of ZigZag path found in the subtree rooted at 'node'.
            """
            if not node:
                return [-1, -1, 0]  # Base case: no path in an empty node

            left = helper(node.left)
            right = helper(node.right)

            # Calculate the ZigZag path lengths going left and right from the current node
            left_len = left[1] + 1
            right_len = right[0] + 1

            # The maximum length of a ZigZag path in the subtree is the maximum of the left and right lengths
            max_len = max(left_len, right_len, left[2], right[2])

            return [left_len, right_len, max_len]

        # Start the helper function from the root
        return helper(root)[2]

# Example usage
# Assume a valid TreeNode root is given
sol = Solution()
print(sol.longestZigZag(root))  # Output will be the length of the longest ZigZag path
