# 222. Count Complete Tree Nodes

# Correct Approach: Improved nodeExists function over my original one
class Solution:
    def getHeight(self, n):
        if not n:
            return 0
        return self.getHeight(n.left) + 1

    def nodeExists(self, root, height, ind):
        l = 0
        r = self.lenLast - 1
        count = 1
        node = root  # renaming for better readability

        while count < height:
            mid = (l + r) // 2

            if ind <= mid:
                r = mid
                node = node.left
            elif ind > mid:
                l = mid + 1
                node = node.right

            count += 1

        return node is not None

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        h = self.getHeight(root)

        nodesBeforeLast = (2 ** (h-1)) - 1
        self.lenLast = (2 ** (h - 1))

        l = 0
        r = self.lenLast - 1

        if self.nodeExists(root, h, r):
            return nodesBeforeLast + self.lenLast

        while l < r:
            mid = (l + r) // 2

            if self.nodeExists(root, h, mid):
                l = mid + 1
            else:
                r = mid

        return nodesBeforeLast + l


# My original approach: correct but thinking about l != r logic in nodeExists can be tricky
class Solution:
    def getHeight(self, n):
        if not n:
            return 0
        return self.getHeight(n.left) + 1
    
    def nodeExists(self, root, ind):
        l = 0
        r = self.lenLast - 1
        node = root
        
        while l != r:
            mid = (l + r) // 2
            
            if ind <= mid:
                r = mid
                node = node.left
            elif ind > mid:
                l = mid + 1
                node = node.right
        
        return node is not None
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        h = self.getHeight(root)
        
        nodesBeforeLast = (2 ** (h-1)) - 1
        self.lenLast = (2 ** (h - 1))
        
        l = 0
        r = self.lenLast - 1
        
        if self.nodeExists(root, r):
            return nodesBeforeLast + self.lenLast
        
        while l < r:
            mid = (l + r) // 2
            
            if self.nodeExists(root, mid):
                l = mid + 1
            else:
                r = mid
        
        return nodesBeforeLast + l