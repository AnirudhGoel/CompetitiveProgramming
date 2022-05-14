# 2096. Step-By-Step Directions From a Binary Tree Node to Another

# Solution 2: With DFS (much faster)
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfsPath(node, dest, path):
            if not node:
                return
            
            path.append('L')
            if dfsPath(node.left, dest, path):
                return path
            path.pop()
            
            if node.val == dest:
                return path
            
            path.append('R')
            if dfsPath(node.right, dest, path):
                return path
            path.pop()
        
        rootToS = dfsPath(root, startValue, [])
        
        rootToD = dfsPath(root, destValue, [])
        
        i = 0
        
        while i < len(rootToS) and i < len(rootToD) and rootToS[i] == rootToD[i]:
            i += 1
        
        left = ['U'] * (len(rootToS) - i)
        leftStr = ''.join(left)
        
        rightStr = ''.join(rootToD[i:])
        
        return leftStr + rightStr


# Solution 1: The answer is correct but gives TLE because when we append new items to the queue, we create a new list every time when we concatenate to the list, which has a time complexity of O(n) every time
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def bfsPath(node, dest):
            q = deque()
            
            # format of q elements is [node, path], using list for path cz editing it is easier
            q.append([node, []])
            
            while q:
                node, path = q.popleft()
                
                if node.val == dest:
                    return path
                
                if node.left:
                    q.append([node.left, path + ['L']])
                    
                if node.right:
                    q.append([node.right, path + ['R']])
        
        rootToS = bfsPath(root, startValue)
        
        rootToD = bfsPath(root, destValue)
        
        i = 0
        
        while i < len(rootToS) and i < len(rootToD) and rootToS[i] == rootToD[i]:
            i += 1
        
        left = ['U'] * (len(rootToS) - i)
        leftStr = ''.join(left)
        
        rightStr = ''.join(rootToD[i:])
        
        return leftStr + rightStr