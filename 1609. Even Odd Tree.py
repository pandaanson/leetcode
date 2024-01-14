# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        level = 0
        queue = deque([root])

        while queue:
            if level%2==0:
                mode='even'
            else:
                mode='odd'
            first=True
            level_size = len(queue)



            for _ in range(level_size):
                node = queue.popleft()
                if first:
                    first=False
                    if (mode=='even' and node.val%2==0) or (mode=='odd' and node.val%2==1):
                        return False
                    
                else:
                    if (mode=='even' and (node.val%2==0 or node.val<=temp)) or (mode=='odd' and (node.val%2==1 or node.val>=temp)):
                        return False
                temp=node.val
                    


                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


            level += 1

        return True
