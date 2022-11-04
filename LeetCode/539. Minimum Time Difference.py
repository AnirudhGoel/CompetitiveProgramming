# 539. Minimum Time Difference

# Solution 1: Only tricky part was sorting and then thinking about the last case where we check difference between last time of the day and first time of the day
# Imagine the sorting as putting all the minutes on a timeline of a single day
# T: O(logN) due to sorting
import heapq

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        day_end_min = 24 * 60
        day_start_min = 0
        min_diff = float('inf')
        
        distance_from_midnight_list = list()
        
        for timePoint in timePoints:
            hour, minute = timePoint.split(':')
            time_point_in_min = int(hour) * 60 + int(minute)
            
            distance_from_midnight_list.append(time_point_in_min)
        
        distance_from_midnight_list.sort()
        
        for i in range(len(distance_from_midnight_list) - 1):
            min_diff = min(min_diff, distance_from_midnight_list[i+1] - distance_from_midnight_list[i])
        
        min_diff = min(min_diff, abs(1440 - distance_from_midnight_list[-1] + distance_from_midnight_list[0]))
        
        return min_diff