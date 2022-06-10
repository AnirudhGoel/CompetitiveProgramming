#323. Number of Connected Components in an Undirected Graph

# Solution 1: DFS 99.68% faster in 1st attempt
class Solution:
    def dfs(self, adj_list, unvisited, v):
        for adj in adj_list[v]:
            if adj in unvisited:
                unvisited.remove(adj)
                self.dfs(adj_list, unvisited, adj)
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        components = 0
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        unvisited = {i for i in range(n)}
        
        while unvisited:
            v = unvisited.pop()
            components += 1
            
            self.dfs(adj_list, unvisited, v)
        
        return components