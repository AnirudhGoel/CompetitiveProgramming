# 1146. Snapshot Array

# Solution 2: Took help from discussion section (94% faster) - Important Memoization
class SnapshotArray:
    def __init__(self, length: int):
        self.snapMap = dict()
        self.snap_no = 0

    def set(self, index: int, val: int) -> None:
        self.snapMap[index] = self.snapMap.get(index, dict())
        self.snapMap[index][self.snap_no] = val

    def snap(self) -> int:
        self.snap_no += 1
        return self.snap_no - 1

    def get(self, index: int, snap_id: int) -> int:
        max_snap = -1
        
        if index not in self.snapMap:
            return 0
        
        if snap_id in self.snapMap[index]:
            return self.snapMap[index][snap_id]
        
        # if current snap_id doesn't exist, find last snap_id that exists and memoize it
        for i in range(snap_id, -1, -1):
            if i in self.snapMap[index]:
                self.snapMap[index][snap_id] = self.snapMap[index][i]
                return self.snapMap[index][snap_id]
        
        return 0


# Solution 1: Correct but exceeds Memory limit
class SnapshotArray:
    def __init__(self, length: int):
        self.snap_no = 0
        self.length = length
        self.arr = {
            self.snap_no: [0 for _ in range(length)]
        }

    def set(self, index: int, val: int) -> None:
        self.arr[self.snap_no][index] = val

    def snap(self) -> int:
        self.snap_no += 1
        self.arr[self.snap_no] = [x for x in self.arr[self.snap_no-1]]
        
        return self.snap_no - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.arr[snap_id][index]