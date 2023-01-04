# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, node: Optional[TreeNode], targetSum: int) -> bool:
        if node is None:
            return False
        if node.val == targetSum and node.left == None and node.right == None:
            return True
        if self.hasPathSum(node.left, targetSum-node.val) or self.hasPathSum(node.right, targetSum-node.val):
            return True