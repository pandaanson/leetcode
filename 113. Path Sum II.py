# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        stack=[]
        if root:
            stack.append([root.val,[root.val],root])#[CurrectSum,Patharr,rawroot]
        while stack:
            tempval,temppath,temproot=stack.pop()
            if not temproot.left and not temproot.right:#If this is a leaf
                if tempval==targetSum:#Check does it reach the target sum
                    ans.append(temppath)
            else:
                if temproot.left:
                    stack.append([tempval+temproot.left.val,temppath+[temproot.left.val],temproot.left])
                if temproot.right:
                    stack.append([tempval+temproot.right.val,temppath+[temproot.right.val],temproot.right])
        return ans
