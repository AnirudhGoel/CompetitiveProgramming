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

# Solution 2: Union Find Approach (without rank for Union but with Path Compression in Find)
class Solution:
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        find_u = self.find(u)
        find_v = self.find(v)

        if find_u == find_v:
            return

        self.parent[max(find_u, find_v)] = min(find_u, find_v, self.parent[max(find_u, find_v)])

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        components_seen = set()

        self.parent = [i for i in range(n)]

        for u, v in edges:
            self.union(u, v)

        for i in self.parent:
            if self.find(self.parent[i]) not in components_seen:
                components += 1
                components_seen.add(self.parent[i])

        return components