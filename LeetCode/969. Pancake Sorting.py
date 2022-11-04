# 969. Pancake Sorting

# Solution 1:
# Find the max number from array and place it at the last position and continue for every position from right to left
# 1 2 5 3 4
# Flip 1: k = position of maximum element
# 5 2 1 3 4
# Flip 2: k = position where you want to place the max element
# 4 3 1 2 5
# T: O(N^2)
class Solution:
    def flip(self, arr, k):
        for i in range(ceil(k/2)):
            arr[i], arr[k-i] = arr[k-i], arr[i]
        return arr
    
    def pancakeSort(self, arr: List[int]) -> List[int]:
        sort_idx = len(arr) - 1
        final_list = list()
        
        while sort_idx >= 0:
            max_idx = -1
            max_val = -1
            
            for i in range(sort_idx + 1):
                if arr[i] > max_val:
                    max_val = arr[i]
                    max_idx = i
            
            if max_idx == sort_idx:
                sort_idx -= 1
                continue
            
            self.flip(arr, max_idx)
            self.flip(arr, sort_idx)
            
            final_list.append(max_idx + 1)
            final_list.append(sort_idx + 1)

            sort_idx -= 1
        
        return final_list