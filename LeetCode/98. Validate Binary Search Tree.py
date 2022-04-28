# 98. Validate Binary Search Tree

# My Approach (85% faster): All correct and very similar to official solution except they used single var to store last value instead of array
class Solution:
    def inorder(self, node, values):
        if not node:
            return True
        
        if not self.inorder(node.left, values):
            return False
        
        if values and node.val <= values[-1]:
            return False
        
        values.append(node.val)
        
        if not self.inorder(node.right, values):
            return False
        
        return True
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = list()
        
        return self.inorder(root, values)

# Approach 2
class Solution:
    def validate(self, lower, upper, node):
        if not node:
            return True

        if not lower < node.val < upper:
            return False

        if not self.validate(lower, node.val, node.left):
            return False

        if not self.validate(node.val, upper, node.right):
            return False

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(float('-inf'), float('inf'), root)