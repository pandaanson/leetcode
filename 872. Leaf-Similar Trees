class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafarrfinder(tree):
            ans=[]
            if not tree.left and not tree.right:
                return [tree.val]
            if tree.left:
                ans+=leafarrfinder(tree.left)
            if tree.right:
                ans+=leafarrfinder(tree.right)
            return ans
        return leafarrfinder(root1)==leafarrfinder(root2)
