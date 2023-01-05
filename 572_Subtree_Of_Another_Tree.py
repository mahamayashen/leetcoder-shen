# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubtree(self, node: Optional[TreeNode], subNode: Optional[TreeNode]) -> bool:
        if node and not subNode:
            return True
        if not node and subNode:
            return False
        if self.isidentical(node, subNode):
            return True
        return (self.isSubtree(node.left, subNode) or self.isSubtree(node.right, subNode))


    def isidentical(self, node: Optional[TreeNode], subNode) -> bool:
        if not node and not subNode:
            return True
        if (not node and subNode) or (node and not subNode):
            return False
        if node.val == subNode.val:
            leftpart = self.isidentical(node.left, subNode.left)
            rightpart = self.isidentical(node.right, subNode.right)    
            return (leftpart and rightpart)