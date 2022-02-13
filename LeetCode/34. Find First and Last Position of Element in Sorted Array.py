# 34. Find First and Last Position of Element in Sorted Array

# Solution 1: Use binary search to find the first element and then linear search on both sides to find start and end elements
# Works but in worst case time complexity can be O(n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        mid = int((r+l)/2)
        start = -1
        end = -1
        
        while 0 <= l <= r <= (len(nums) - 1):
            if target > nums[mid]:
                l = mid + 1
                mid = int((r+l)/2)
            elif target < nums[mid]:
                r = mid - 1
                mid = int((r+l)/2)
                
            if target == nums[mid]:
                start = end = mid

                while start > 0 and nums[start-1] == target:
                    start -= 1
                
                while end < (len(nums) - 1) and nums[end+1] == target:
                    end += 1

                break
        
        return [start, end]


# Solution 2: 95% faster (YAY!)
class Solution:
    def findStartIndex(self, n, t):
        l = 0
        r = len(n) - 1

        while l <= r:
            mid = (l + r) // 2

            if t == n[mid]:
                # if the mid element is equal to target we only want to return its index if the same element doesn't appear before the mid element (or mid = 0)
                if mid == 0 or n[mid-1] != t:
                    return mid
                r = mid - 1
            elif t > n[mid]:
                # if mid == len(n) - 1:
                #     break
                # we don't need to check the above condition cz this is only possible when len(n) = 1 and in that case l = mid + 1 will make l > r

                l = mid + 1
            else:
                r = mid - 1

        return(-1)

    def findEndIndex(self, n, t):
        l = 0
        r = len(n) - 1

        while l <= r:
            mid = (l + r) // 2

            if t == n[mid]:
                if mid == (len(n)-1) or n[mid+1] != t:
                    return mid
                l = mid + 1
            elif t > n[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return(-1)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2

        start = self.findStartIndex(nums, target)

        if start == -1:
            return [-1, -1]

        end = self.findEndIndex(nums, target)

        return [start, end]