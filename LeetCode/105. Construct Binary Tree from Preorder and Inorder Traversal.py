# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Solution: Solved on my own, in a little over 40 mins - The key was to write test cases and find a pattern (see in iPad)
# But the time complexity for this is O(N^2) because I'm using the .index() function
# Can be easily converted to O(N) by storing the values of inorder list as key in a dict with their indexes as values
class Solution:
    def construct(self, preorder, inorder):
        curr_node = TreeNode()
        curr_node.val = preorder[self.preorder_idx]
        
        inorder_idx = inorder.index(preorder[self.preorder_idx])

        if inorder_idx > 0:
            self.preorder_idx += 1
            curr_node.left = self.construct(preorder, inorder[:inorder_idx])

        if inorder_idx < len(inorder) - 1:
            self.preorder_idx += 1
            curr_node.right = self.construct(preorder, inorder[inorder_idx+1:])

        return curr_node
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return []
        
        self.preorder_idx = 0
        
        return self.construct(preorder, inorder)