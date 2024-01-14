#BFS
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        stack=[root]
        tempstack=[]
        ans=0
        while stack or tempstack:
            temp=stack.pop()
            ans+=temp.val
            if temp.left:
                tempstack.append(temp.left)
            if temp.right:
                tempstack.append(temp.right)
            if (not stack) and tempstack:
                while tempstack:
                    stack.append(tempstack.pop())
                ans=0
        return ans
#DFS
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if not root.left and not root.right:
                return [1,root.val]
            if root.left:
                leftr=helper(root.left)
            else:
                leftr=[0,0]
            if root.right:
                rightr=helper(root.right)
            else:
                rightr=[0,0]
            if leftr[0]==rightr[0]:
                return [rightr[0]+1,rightr[1]+leftr[1]]
            elif leftr[0]>rightr[0]:
                return [leftr[0]+1,leftr[1]]
            else:
                return [rightr[0]+1,rightr[1]]
        return helper(root)[1]
 
