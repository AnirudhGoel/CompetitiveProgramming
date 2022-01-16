class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        l = 0
        r = len_nums - 1
        ptr = r
        res = [None for i in range(len_nums)]
        
        while ptr >= 0:
            if abs(nums[l]) >= abs(nums[r]):
                res[ptr] = nums[l] ** 2
                l += 1
            else:
                res[ptr] = nums[r] ** 2
                r -= 1
            ptr -= 1
        
        return(res)