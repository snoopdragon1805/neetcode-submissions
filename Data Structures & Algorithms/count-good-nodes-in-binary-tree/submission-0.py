# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.count = 0

        def helper(cur, m):
            if cur.val>=m:
                self.count+=1
                m = cur.val
            if cur.left:
                helper(cur.left,m)
            if cur.right:
                helper(cur.right,m)
        
        helper(root,root.val)
        return self.count

