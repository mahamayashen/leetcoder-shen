# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, node: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.fin_lists = []

        def pathlist(node, sequence, curr_sum):
            if not node:
                return
            sequence.append(node.val)
            if (not node.left and not node.right) and (curr_sum + node.val == targetSum):
                self.fin_lists.append([*sequence])
            
            pathlist(node.left, sequence, curr_sum + node.val)
            pathlist(node.right, sequence, curr_sum + node.val)
                
            sequence.pop()

        pathlist(node, [], 0)
        return self.fin_lists