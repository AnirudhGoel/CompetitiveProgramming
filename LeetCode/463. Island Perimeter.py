# 463. Island Perimeter

from collections import deque

class Solution:
    def islandExists(self, grid, x, y):
        return True if 0 <= x < self.numRows and 0 <= y < self.numCols and grid[x][y] in (1, -1) else False
    
    def getNeighbours(self, grid, x, y):
        unvisitedNeighbours = list()
        count = 0  # count keeps track of all (visited + unvisited) neighbour because even if they have been visited, their shared edges needs to be subtracted
        neighCoordinates = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for n in neighCoordinates:
            if self.islandExists(grid, x + n[0], y + n[1]):
                count += 1
                if grid[x + n[0]][y + n[1]] == 1:
                    grid[x + n[0]][y + n[1]] = -1
                    unvisitedNeighbours.append([x + n[0], y + n[1]])
                
        return unvisitedNeighbours, count
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.numRows = len(grid)
        self.numCols = len(grid[0])
        perimeter = 0

        for row in range(self.numRows):
            for col in range(self.numCols):
                if grid[row][col] == 1:
                    break
            else:
                continue
            break
        
        q = deque([[row, col]])
        grid[row][col] = -1
        
        while q:
            curr_node = q.popleft()
            
            unvisitedNeighbours, count = self.getNeighbours(grid, *curr_node)
            
            perimeter += 4 - count
            
            q.extend(unvisitedNeighbours)
        
        return perimeter