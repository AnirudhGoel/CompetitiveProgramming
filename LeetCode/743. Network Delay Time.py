# 743. Network Delay Time

# Solution 1: Dijkstra Algo after watching Udemy Video
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_mat = [[float('inf') for _ in range(n)] for _ in range(n)]
        k -= 1  # adjusting k for 0 indexed everything
        visited = set()
        
        for row in range(n):
            for col in range(n):
                if row == col:
                    adj_mat[row][col] = 0
        
        min_cost_neigh = []
        heapq.heapify(min_cost_neigh)
        
        for time in times:
            u, v, w = time
            adj_mat[u-1][v-1] = w  # adjusting k for 0 indexed everything
        
        source = k
        visited.add(source)
        
        for dest in range(n):
            dest_w = adj_mat[source][dest]
            if dest_w < float('inf') and dest not in visited:
                heapq.heappush(min_cost_neigh, [dest_w, dest])

        while min_cost_neigh:
            _, min_cost_dest = heapq.heappop(min_cost_neigh)
            visited.add(min_cost_dest)
            
            for dest in range(n):
                dest_w = adj_mat[min_cost_dest][dest]
                
                adj_mat[source][dest] = min(adj_mat[source][dest], adj_mat[source][min_cost_dest] + adj_mat[min_cost_dest][dest])
                
                if dest_w < float('inf') and dest not in visited:
                    heapq.heappush(min_cost_neigh, [dest_w, dest])
        
        final_cost_list = adj_mat[source]
        
        return -1 if max(final_cost_list) == float('inf') else max(final_cost_list)

# Solution 2: Plain BFS, on my own, as practice
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]

        for i in range(len(times)):
            adj_list[times[i][0] - 1].append([times[i][1] - 1, times[i][2]])  # adjusting for nodes labelled from 1

        travel_time = [float('inf') for _ in range(n)]
        q = deque()
        q.append(k-1)
        travel_time[k-1] = 0

        while q:
            curr_node = q.popleft()

            for adj, time in adj_list[curr_node]:
                if travel_time[curr_node] + time < travel_time[adj]:
                    travel_time[adj] = travel_time[curr_node] + time
                    q.append(adj)

        return max(travel_time) if max(travel_time) != float('inf') else -1

# Solution 3: Djikstra Algo on my own, for practice
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dj_time = [float('inf') for _ in range(n)]
        dj_time[k-1] = 0

        adj_list = [[] for _ in range(n)]
        for u, v, w in times:
            adj_list[u-1].append([v-1, w])

        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, [0, k-1])

        visited = set()

        while heap:
            curr_time, curr_node = heapq.heappop(heap)

            if curr_node in visited:
                continue

            visited.add(curr_node)

            for v, w in adj_list[curr_node]:
                if curr_time + w < dj_time[v]:
                    dj_time[v] = curr_time + w
                    heapq.heappush(heap, [curr_time + w, v])

        return -1 if max(dj_time) == float('inf') else max(dj_time)