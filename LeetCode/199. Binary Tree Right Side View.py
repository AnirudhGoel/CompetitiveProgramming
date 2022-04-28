# 199. Binary Tree Right Side View

# My Solution: Do Postorder Traversal and then read the list from right and take first value for every level
class Solution:
    def postOrderDFS(self, root, level):
        if root is None:
            level -= 1
            return
        
        self.postOrderDFS(root.left, level+1)
        self.postOrderDFS(root.right, level+1)
        
        self.nodeList.append([root.val, level])
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        
        self.nodeList = list()
        maxLevel = 0
        finalList = list()
        
        self.postOrderDFS(root, 1)
        
        self.nodeList.reverse()
        
        for n in self.nodeList:
            val = n[0]
            level = n[1]
            
            if level > maxLevel:
                maxLevel = max(maxLevel, level)
                finalList.append(val)
            
        return finalList

# Solution 2: Faster solution from leetcode
# Do postorder traversal with RLN instead of LRN and then just take one value for every new level
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l = defaultdict(list)
        def dfs(node, h):
            if not node: return
            if h not in l:
                l[h] = node.val

            dfs(node.right, h+1)
            dfs(node.left, h+1)
        dfs(root, 0)
        return [v for k,v in l.items()]
