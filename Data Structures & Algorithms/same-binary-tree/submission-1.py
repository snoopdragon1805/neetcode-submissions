# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checker(p,q):
            if p and q:
                l = checker(p.left,q.left)
                if l == -1:
                    return -1
                r = checker(p.right,q.right)
                if r == -1:
                    return -1
                if p.val == q.val:
                    return 0
                else:
                    return -1
            if (not p and q) or (p and not q):
                return -1
            if not p and not q:
                return 0
        return checker(p,q)==0
                

                