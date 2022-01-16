200. Number of Islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        count = 0

        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid, numRows, numCols)
                    count += 1
                        
        return(count)
    
    def dfs(self, i, j, grid, numRows, numCols):
        if 0 <= i < numRows and 0 <= j < numCols:
            if grid[i][j] == '1':
                grid[i][j] = '0'

                self.dfs(i+1, j, grid, numRows, numCols)
                self.dfs(i-1, j, grid, numRows, numCols)
                self.dfs(i, j+1, grid, numRows, numCols)
                self.dfs(i, j-1, grid, numRows, numCols)