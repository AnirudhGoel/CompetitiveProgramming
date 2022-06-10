# 329. Longest Increasing Path in a Matrix

# Solution 1: Correct in first attempt, even for testcases! Yay!
# DFS + Memoization - Similar to Approach 2 in Leetcode Solution
class Solution:
    def getValidAdjacent(self, matrix, row, col):
        adjacents = list()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        for x, y in directions:
            if 0 <= row + x < len(matrix) and 0 <= col + y < len(matrix[0]) and matrix[row+x][col+y] > matrix[row][col]:
                adjacents.append([row + x, col + y])
        
        return adjacents
        
    def dfs(self, matrix, path_length, row, col):
        adjacents = self.getValidAdjacent(matrix, row, col)
        
        if not adjacents:
            return 1
        
        for x, y in adjacents:
            if path_length[x][y] != -1:
                path_length[row][col] = max(path_length[row][col], path_length[x][y] + 1)
            else:
                path_length[row][col] = max(path_length[row][col], self.dfs(matrix, path_length, x, y) + 1)
        
        return path_length[row][col]
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        path_length = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        longest_path_len = 1
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if path_length[row][col] == -1:
                    longest_path_len = max(longest_path_len, self.dfs(matrix, path_length, row, col))
                    
                    
        return longest_path_len