# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, mVal):
            if not node:
                return 0
            if node.val >= mVal:
                res = 1
                mVal = node.val
            else:
                res = 0
            return res + dfs(node.right, mVal) + dfs(node.left, mVal)
        return dfs(root, root.val)
            