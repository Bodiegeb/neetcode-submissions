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
            res = 0
            res = 1 if node.val >= mVal else 0
            mVal = max(mVal, node.val)
            res += dfs(node.left, mVal)
            res += dfs(node.right, mVal)
            return res
        return dfs(root, root.val)
            