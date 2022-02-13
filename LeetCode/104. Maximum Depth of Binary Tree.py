# 104. Maximum Depth of Binary Tree

# Solution 1: Proper solution
class Solution:    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Solution 2: Flex one line solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0

# Solution 3: Basic intuitive but inefficient solution
# Inefficient because you are using 2 vars - depth and max_depth and then calculating the max between those rather, because it is a tree question where you have only 2 branches you can just calculate the max between the left and right sub branches. See solution 4 from Udemy guy
class Solution:
    def dfs(self, n):
        if not n:
            self.max_depth = max(self.max_depth, self.depth)
            return

        self.depth += 1
        self.dfs(n.left)
        self.dfs(n.right)
        self.depth -= 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        self.max_depth = 0

        self.dfs(root)

        return(self.max_depth)

# Solution 4:
# This also increments the depth going downwards and stores it in a var, but still "shorter" than mine because it runs max on the left and right sub-trees. Also note that because you have to maintain this extra var 'depth', you have to write dfs as a separate function.
class Solution:
    def dfs(self, node, d):
        if not node:
            return d

        d += 1
        return(max(self.dfs(node.left, d), self.dfs(node.right, d)))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        return self.dfs(root, depth)