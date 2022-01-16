# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = list()
        visited = list()

        if not root:
            return([])

        stack.append(root)

        while stack:
            node = stack[-1]

            while node.left and node.left not in visited:
                stack.append(node.left)

            visited.append(stack[-1])
            stack.pop()

            if node.right and node.right not in visited:
                stack.append(node.right)

        return([node.val for node in visited])