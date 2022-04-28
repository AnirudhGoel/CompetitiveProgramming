# 63. Unique Paths II

# 97% faster
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        ans = [[-1] * col] * row
        
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    ans[i][j] = 1 if obstacleGrid[i][j] == 0 else 0
                elif obstacleGrid[i][j] == 1:
                    ans[i][j] = 0
                elif i == 0 or j == 0:
                    if (i == 0 and ans[i][j-1] == 0) or (j == 0 and ans[i-1][j] == 0):
                        ans[i][j] = 0
                    else:
                        ans[i][j] = 1
                else:
                    ans[i][j] = ans[i-1][j] + ans[i][j-1]

        return(ans[row-1][col-1])