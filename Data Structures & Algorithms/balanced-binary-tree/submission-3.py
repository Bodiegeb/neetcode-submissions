# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def dfs(root):
            if not root:
                return True
            nonlocal isBalanced
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            if (leftHeight - rightHeight) > 1 or (rightHeight - leftHeight) > 1:
                isBalanced = False
            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return isBalanced