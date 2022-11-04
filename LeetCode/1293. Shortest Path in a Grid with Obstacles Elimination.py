# 1293. Shortest Path in a Grid with Obstacles Elimination

# Solution 1: Using individual visited sets in each element in the queue (TLE)
class Solution:
    def getValidAdjacents(self, m, n, row, col):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        adjacents = list()
        
        for x, y in directions:
            if 0 <= row + x < m and 0 <= col + y < n:
                adjacents.append([row + x, col + y])
        
        return adjacents
    
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        if m == 1 and n == 1:
            return 0

        q = deque()
        
        # format of q elements: [row, col, obstacles, steps, visited_set]
        q.append([0, 0, 0, 0, {(0, 0), }])
        
        while q:
            row, col, obs, steps, visited = q.popleft()
            
            adjacents = self.getValidAdjacents(m, n, row, col)
            
            for adjacent in adjacents:
                x, y = adjacent
                
                if x == m-1 and y == n-1:
                    return steps + 1
                
                if (x, y) not in visited:
                    if grid[x][y] == 1 and obs < k:
                        new_visited = visited.copy()
                        new_visited.add((x, y))
                        q.append([x, y, obs + 1, steps + 1, new_visited])
                        
                    elif grid[x][y] == 0:
                        new_visited = visited.copy()
                        new_visited.add((x, y))
                        q.append([x, y, obs, steps + 1, new_visited])
        
        return -1


# Solution 2: Using defaultdict for maintaining visited
class Solution:
    def getValidAdjacents(self, m, n, row, col):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        adjacents = list()
        
        for x, y in directions:
            if 0 <= row + x < m and 0 <= col + y < n:
                adjacents.append([row + x, col + y])
        
        return adjacents
    
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[[False for _ in range(k + 1)] for _ in range(n)] for _ in range(m)]
        
        if m == 1 and n == 1:
            return 0

        q = deque()
        
        # format of q elements: [row, col, obstacles, steps]
        q.append([0, 0, 0, 0])
        
        while q:
            row, col, obs, steps = q.popleft()
            
            adjacents = self.getValidAdjacents(m, n, row, col)
            
            for adjacent in adjacents:
                x, y = adjacent
                
                if x == m-1 and y == n-1:
                    return steps + 1
                
                if not visited[x][y][obs]:
                    if grid[x][y] == 1 and obs < k:
                        visited[x][y][obs + 1] = True
                        q.append([x, y, obs + 1, steps + 1])
                        
                    elif grid[x][y] == 0:
                        visited[x][y][obs] = True
                        q.append([x, y, obs, steps + 1])
        
        return -1

# Correct Solution
# Was getting TLE because of wrong check
# When checking the visited set, I was checking for (x, y, obs) for both cases, when current cell is obstacle and when it's not
# Whereas if the current cell is an obstacle I should check for (x, y, obs+1)
class Solution:
    def getValidAdjacents(self, m, n, row, col):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        adjacents = list()

        for x, y in directions:
            if 0 <= row + x < m and 0 <= col + y < n:
                adjacents.append([row + x, col + y])

        return adjacents

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()

        if m == 1 and n == 1:
            return 0

        # Manhattan distance trick
        if k >= m + n - 2:
            return m + n - 2

        q = deque()

        # format of q elements: [row, col, obstacles, steps]
        q.append([0, 0, 0, 0])
        visited.add((0, 0, 0))

        while q:
            row, col, obs, steps = q.popleft()

            adjacents = self.getValidAdjacents(m, n, row, col)

            for adjacent in adjacents:
                x, y = adjacent

                if x == m-1 and y == n-1:
                    return steps + 1

                if grid[x][y] == 1 and obs < k and (x, y, obs+1) not in visited:
                    visited.add((x, y, obs + 1))
                    q.append([x, y, obs + 1, steps + 1])

                elif grid[x][y] == 0 and (x, y, obs) not in visited:
                    visited.add((x, y, obs))
                    q.append([x, y, obs, steps + 1])

        return -1