# 994. Rotting Oranges

# Solution 1
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def notReachable(x, y):
            pass
        
        
        def getFreshNeigh(x, y):
            neigh = list()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            for i, j in directions:
                if 0 <= x+i < len(grid) and 0 <= y+j < len(grid[0]) and grid[x+i][y+j] == 1:
                    neigh.append([x+i, y+j])
                    grid[x+i][y+j] = 2
            
            return neigh
        
        
        fresh = 0
        rotten = deque()  # rotten will have format [x, y, time]
        time = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    fresh += 1
                    
                    # if notReachable(x, y):
                    #     return -1
                elif grid[x][y] == 2:
                    rotten.append([x, y, time])
            
            total_orange = fresh + len(rotten)
            total_rotted = len(rotten)
            
        while rotten:
            x, y, time = rotten.popleft()

            fresh_neigh = getFreshNeigh(x, y)

            for i, j in fresh_neigh:
                rotten.append([i, j, time+1])
                total_rotted += 1
            
        return time if total_orange == total_rotted else -1


# Solution 2: With added optimisation for checking if a fresh orange is not reachable beforehand, but is slower than my original solution
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def notReachable(x, y):
            neigh_count = 0
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            for i, j in directions:
                if 0 <= x+i < len(grid) and 0 <= y+j < len(grid[0]) and grid[x+i][y+j] in (1, 2):
                    neigh_count += 1
            
            return (neigh_count == 0)
        
        
        def getFreshNeigh(x, y):
            neigh = list()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            for i, j in directions:
                if 0 <= x+i < len(grid) and 0 <= y+j < len(grid[0]) and grid[x+i][y+j] == 1:
                    neigh.append([x+i, y+j])
                    grid[x+i][y+j] = 2
            
            return neigh
        
        
        fresh = 0
        rotten = deque()  # rotten will have format [x, y, time]
        time = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    fresh += 1
                    
                    if notReachable(x, y):
                        return -1
                elif grid[x][y] == 2:
                    rotten.append([x, y, time])
            
            total_orange = fresh + len(rotten)
            total_rotted = len(rotten)
            
        while rotten:
            x, y, time = rotten.popleft()

            fresh_neigh = getFreshNeigh(x, y)

            for i, j in fresh_neigh:
                rotten.append([i, j, time+1])
                total_rotted += 1
            
        return time if total_orange == total_rotted else -1