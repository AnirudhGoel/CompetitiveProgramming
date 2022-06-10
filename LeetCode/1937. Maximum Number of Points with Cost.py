# 1937. Maximum Number of Points with Cost

# Solution 1: Greedy Solution
# For every element in the first row, calculate the best score by iterating through all other rows
# But this approach fails when there are two points in the next to current row where the score will be the same
# but in the next to next row, there's a number that makes one "next" row better than the other
# For example - [[0,0,4,1,4],[2,1,2,0,1],[2,2,1,3,4],[5,2,4,5,4],[0,5,4,2,5]]
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def getPoints(curr_row, y1, y2):
            return points[curr_row][y2] - abs(y1 - y2)
        
        max_total_points = 0
        total_points = 0
        prev_x = 0
        
        for start in range(len(points[0])):
            prev_y = start
            total_points = points[0][start]
            
            for i in range(1, len(points)):
                curr_x = i
                curr_row_max_point = -1
                
                for j in range(len(points[0])):
                    curr_y = j
                    curr_point = getPoints(curr_x, prev_y, curr_y)
                    
                    if curr_point > curr_row_max_point:
                        curr_row_max_y = curr_y
                        curr_row_max_point = curr_point
                
                prev_y = curr_row_max_y
                total_points += curr_row_max_point
            
            max_total_points = max(max_total_points, total_points)
        
        return max_total_points

# Solution 2: Explanation in iPad
# Time: O(N), Space: O(1)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        for row in range(len(points) - 1):
            for col in range(1, len(points[0])):
                points[row][col] = max(points[row][col], points[row][col-1] - 1)

            for col in range(len(points[0]) - 2, -1, -1):
                points[row][col] = max(points[row][col], points[row][col+1] - 1)

            for col in range(len(points[0])):
                points[row+1][col] += points[row][col]

        return max(points[-1])