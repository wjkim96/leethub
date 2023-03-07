# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderHelp(self, node, ans):
        if not node:
            return
        
        self.inorderHelp(node.left, ans)
        ans.append(node.val)
        self.inorderHelp(node.right, ans)
              
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.inorderHelp(root, ans)
        return ans
            
            