# 218. The Skyline Problem
# Different approach than the leetcode solution
# Thought on my own - similar to this https://www.youtube.com/watch?v=GSBLe8cKu0s&t=820s&ab_channel=TusharRoy-CodingMadeSimple

import heapq
from collections import deque

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        index = 0
        height_heap = list()
        l = list()
        r = list()
        res = list()
        
        heapq.heapify(height_heap)
        
        for b in buildings:
            l.append([b[0], b[2], index])
            r.append([b[1], b[2], index])
            index += 1
        
        l.sort(key=lambda i: i[0])
        r.sort(key=lambda i: i[0])
        
        left = deque(l)
        right = deque(r)
        
        building_exists = dict()
        
        while right:
            if left and left[0][0] <= right[0][0]:
                curr = left.popleft()
                curr_x = curr[0]
                curr_height = curr[1]
                curr_index = curr[2]
                
                building_exists[curr_index] = True
                
                if not len(height_heap) or curr_height > -height_heap[0][0]:
                    if res and res[-1][0] == curr_x:
                        res[-1][1] = max(res[-1][1], curr_height)
                    else:
                        res.append([curr_x, curr_height])
                
                heapq.heappush(height_heap, [-curr_height, curr_index])
            elif not left or right[0][0] < left[0][0]:
                curr = right.popleft()
                curr_height = curr[1]
                curr_index = curr[2]
                
                building_exists[curr_index] = False

                while height_heap and not building_exists[height_heap[0][1]]:
                    heapq.heappop(height_heap)

                if height_heap and -height_heap[0][0] != res[-1][1]:
                    if res and res[-1][0] == curr[0]:
                        res[-1][1] = -height_heap[0][0]
                    else:
                        res.append([curr[0], -height_heap[0][0]])
                elif not height_heap:
                    if res and res[-1][0] == curr[0]:
                        res[-1][1] = 0
                    else:
                        res.append([curr[0], 0])
        
        return res