# 102. Binary Tree Level Order Traversal

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([[root, ]])
        res = deque([[root.val, ]])

        while q:
            lvl = q.popleft()
            child = []
            childVal = []

            for n in lvl:
                if n.left:
                    child.append(n.left)
                    childVal.append(n.left.val)
                if n.right:
                    child.append(n.right)
                    childVal.append(n.right.val)

            if child:
                q.append(child)
                res.append(childVal)

        return res