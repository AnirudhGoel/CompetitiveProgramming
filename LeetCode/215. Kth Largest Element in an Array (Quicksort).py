# 215. Kth Largest Element in an Array (Quicksort)

# My own implementation of Quicksort after understanding the algo and not seeing any code! Yay!
# Gives correct answer for all but TLE on big input cz probably the selection of pivot (always last element) is not ideal, but correct answer on own implementation, so Yay!
class Solution:
    def quicksort(self, nums, l, r):
        if l >= r or l < 0 or r >= self.len_nums:
            return

        pivot = nums[r]

        i = l
        j = l

        while j <= r:
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        i -= 1

        self.quicksort(nums, l, i-1)
        self.quicksort(nums, i+1, r)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = 0
        self.len_nums = len(nums)
        r = self.len_nums - 1

        self.quicksort(nums, l, r)
        
        return(nums[-k])