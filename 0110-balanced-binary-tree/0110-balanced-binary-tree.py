# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if not root:
            return 0
        left, right = self.height(root.left), self.height(root.right)
        return max(left, right) + 1
    def isBalancedHelp(self, root):
        if not root:
            return True
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        else:
            return True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not self.isBalancedHelp(root):
            return False
        else:
            if not self.isBalanced(root.left):
                return False
            if not self.isBalanced(root.right):
                return False
        return True

        
        