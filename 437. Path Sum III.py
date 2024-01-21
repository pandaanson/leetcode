# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def countPaths(node, currentSum):
            if not node:
                return 0
            currentSum += node.val
            return (currentSum == targetSum) + countPaths(node.left, currentSum) + countPaths(node.right, currentSum)

        def dfs(node):
            if not node:
                return 0
            return countPaths(node, 0) + dfs(node.left) + dfs(node.right)

        return dfs(root)
