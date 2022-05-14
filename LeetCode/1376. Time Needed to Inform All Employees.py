# 1376. Time Needed to Inform All Employees

# My solution: only tricky part was to maintain two times - max_time and curr_path_time without them messing with each other
class Solution:
    def dfs(self, adjList, informTime, curr, curr_path_time, max_time):
        if not adjList[curr]:
            return curr_path_time
        
        for node in adjList[curr]:
            max_time = max(max_time, self.dfs(adjList, informTime, node, curr_path_time+informTime[node], max_time))
        
        return max_time
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = [[] for _ in range(n)]
        
        for i in range(len(manager)):
            if manager[i] != -1:
                adjList[manager[i]].append(i)
        
        curr_path_time = informTime[headID]
        
        return self.dfs(adjList, informTime, headID, curr_path_time, 0)

# My Solution 2: Here the maxTime and currTime part is much simpler because if you think about it, you can initialise maxTime before processing the children at every level as once you start processing the children, you are going to overwrite the maxTime value and then when you return it at the end of the loop, it's parent's maxTime value will be updated as well and so on...
# In these problems, try to avoid passing these maxTime, currTime values as a function argument (if possible) cz it can cause mess.
class Solution:
    def dfs(self, adjList, informTime, currNode):
        if not adjList[currNode]:
            return informTime[currNode]

        maxTime = 0

        for node in adjList[currNode]:
            maxTime = max(maxTime, self.dfs(adjList, informTime, node) + informTime[currNode])

        return maxTime

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = [[] for _ in range(n)]

        for i in range(len(manager)):
            if manager[i] != -1:
                adjList[manager[i]].append(i)

        return self.dfs(adjList, informTime, headID)