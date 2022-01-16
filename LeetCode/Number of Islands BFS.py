class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        count = 0
        queue = []
        row_modifier = [1, -1, 0, 0]
        col_modifier = [0, 0, 1, -1]
        
        def bfs():
            while queue != []:
                i, j = queue.pop(0)

                for x in range(4):
                    if 0 <= i + row_modifier[x] < numRows and 0 <= j + col_modifier[x] < numCols:
                        if grid[i + row_modifier[x]][j + col_modifier[x]] == '1':
                            grid[i + row_modifier[x]][j + col_modifier[x]] = '0'
                            queue.append([i + row_modifier[x], j + col_modifier[x]])
        
        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append([i, j])
                    bfs()
                    count += 1
        
        return(count)