# 286. Walls and Gates

# My Solution 1: Correct but using extra 'dis' var
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def getValidNeigh(i, j):
            neigh = list()
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            
            for x, y in directions:
                if 0 <= x+i < len(rooms) and 0 <= y+j < len(rooms[0]) and rooms[x+i][y+j] not in (0, -1):
                    neigh.append([x+i, y+j])
            
            return neigh
        
        
        gate = deque()
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    gate.append([i, j, 0])
                    
        while gate:
            i, j, dis = gate.popleft()
            
            neigh = getValidNeigh(i, j)
            
            for x, y in neigh:
                if rooms[x][y] > dis + 1:
                    rooms[x][y] = dis + 1
                    gate.append([x, y, dis + 1])

# My Solution 2: Same as above but without extra 'dis' var
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def getValidNeigh(i, j):
            neigh = list()
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

            for x, y in directions:
                if 0 <= x+i < len(rooms) and 0 <= y+j < len(rooms[0]) and rooms[x+i][y+j] not in (0, -1):
                    neigh.append([x+i, y+j])

            return neigh


        gate = deque()

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    gate.append([i, j])

        while gate:
            i, j = gate.popleft()

            neigh = getValidNeigh(i, j)

            for x, y in neigh:
                if rooms[x][y] > rooms[i][j] + 1:
                    rooms[x][y] = rooms[i][j] + 1
                    gate.append([x, y])