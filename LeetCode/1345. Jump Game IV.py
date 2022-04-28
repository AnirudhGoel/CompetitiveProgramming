from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        pos_map = dict()

        for i in range(len(arr)-1, -1, -1):
            if arr[i] in pos_map:
                pos_map[arr[i]].append(i)
            else:
                pos_map[arr[i]] = [i]

        q = deque()
        visited = set()

        # format of queue elements = [index, jumps]
        q.append([0, 0])
        visited.add(0)

        while q:
            i, jumps = q.popleft()

            if i == len(arr) - 1:
                return jumps

            if i+1 < len(arr) and i+1 not in visited:
                q.append([i+1, jumps+1])
                visited.add(i+1)

            if i-1 >= 0 and i-1 not in visited:
                q.append([i-1, jumps+1])
                visited.add(i-1)

            for p in pos_map[arr[i]]:
                if p not in visited:
                    q.append([p, jumps+1])
                    visited.add(p)

                pos_map[arr[i]] = []  # TRICK