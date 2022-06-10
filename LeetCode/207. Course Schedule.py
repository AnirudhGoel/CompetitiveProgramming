# 207. Course Schedule

# Topological Sort: One trick to remember is the last line where instead of checking the indegree dictionary to see if any node has indegree > 0, we just check the number of courses taken against total number of courses. This saves one loop and improves time complexity by a lot.
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        q = list()
        
        for d, s in prerequisites:
            graph[s].append(d)
            indeg[d] += 1
        
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        res = list()
        
        while q:
            course = q.pop()
            res.append(course)  # using this list to check if all courses were taken is a good idea to save one loop
            
            for nextCourse in graph[course]:
                indeg[nextCourse] -= 1
                
                if indeg[nextCourse] == 0:
                    q.append(nextCourse)
        
        return len(res) == numCourses