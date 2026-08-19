# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(max, root):
            if not root:
                return 0
            
            cur = root.val
            if cur >= max:
                max = cur
                self.count += 1
            return dfs(max, root.left) + dfs(max, root.right)
        dfs(root.val, root)
        return self.count