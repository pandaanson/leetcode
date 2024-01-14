class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root):

            
            ans = [root.val, root.val, 0]
            if root.left:
                temp = helper(root.left)
                ans = [min(ans[0], temp[0]), max(ans[1], temp[1]), max(ans[2], temp[2], abs(temp[0] - root.val), abs(temp[1] - root.val))]
            if root.right:
                temp = helper(root.right)
                ans = [min(ans[0], temp[0]), max(ans[1], temp[1]), max(ans[2], temp[2], abs(temp[0] - root.val), abs(temp[1] - root.val))]
            return ans
        
        return helper(root)[2]
