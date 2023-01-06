# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        elif not node.left and not node.right:
            return 1
        elif node.left and node.right:
            return min(self.minDepth(node.left), self.minDepth(node.right)) + 1
        else:
        # if (node.left and not node.right) or (not node.left and node.right):
            return max(self.minDepth(node.left), self.minDepth(node.right)) + 1