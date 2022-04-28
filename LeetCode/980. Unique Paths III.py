# 980. Unique Paths III

# My Approach: BFS
class Solution:
    def getNeigh(self, path_set, last):
        neigh_calc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        i, j = last
        neigh = list()
        
        for modifier in neigh_calc:
            if 0 <= i + modifier[0] < self.row and 0 <= j + modifier[1] < self.col and (i + modifier[0], j + modifier[1]) not in path_set and (i + modifier[0], j + modifier[1]) not in self.obst:
                neigh.append([i + modifier[0], j + modifier[1]])
        
        return neigh
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.row = len(grid)
        self.col = len(grid[0])
        valid = set()
        self.obst = set()
        count = 0
        
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == 0:
                    valid.add((i, j))
                elif grid[i][j] == 1:
                    start = (i, j)
                    valid.add((i, j))
                elif grid[i][j] == 2:
                    end = (i, j)
                    valid.add((i, j))
                elif grid[i][j] == -1:
                    self.obst.add((i, j))
        
        q = deque()
        
        # format of queue = [[path_set, last_node], ...]
        q.append([{start}, start])
        
        while q:
            path_set, last = q.popleft()
            
            if last == end and len(path_set) == len(valid):
                count += 1
                continue
            
            neigh = self.getNeigh(path_set, last)
                        
            for n in neigh:
                updated_set = path_set.copy()
                
                updated_set.add((n[0], n[1]))
                last = (n[0], n[1])
                
                q.append([updated_set, last])
        
        return(count)