# 55. Jump Game

# Approach 1: O(n) but after writing this, I realised it can be done in a single loop instead of 2 loops
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        zero_count = 0
        zero_list = list()
        start_index = 0
        end_index = 0
        
        if nums[0] == 0:
            return True if len(nums) == 1 else False
        
        # if last element is zero, change it to something else because unlike others we have to "just reach" the last element, not cross it
        nums[-1] = 1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                start_index = i if zero_count == 0 else start_index
                zero_count += 1
            elif zero_count != 0:
                end_index = i - 1
                zero_list.append([start_index, end_index, zero_count])
                
                zero_count = 0

        if not zero_list:
            return True
        
        total_zeroes_to_cross = 0
        
        while zero_list:
            curr_start, _, curr_zeroes = zero_list.pop()
            
            if zero_list:
                prev_end = zero_list[-1][1]
            else:
                prev_end = -1
            
            total_zeroes_to_cross += curr_zeroes
            
            for i in range(curr_start-1, prev_end, -1):
                if nums[i] > total_zeroes_to_cross:
                    total_zeroes_to_cross = 0
                    break
                total_zeroes_to_cross += 1
        
        return True if total_zeroes_to_cross == 0 else False

# Approach 2: Similar to first but in one pass
# Traverse from right to left and handle 2 cases:
# 1. If you get zeroes, increment 'zeroes' var and continue
# 2. If you get a non-zero number, check if it is greater than the zeroes you have counted, if not, increment the 'zeroes' var further because the next good index will have to cross this index too.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0:
            return True if len(nums) == 1 else False

        nums[-1] = 1
        zeroes = 0

        for i in range(len(nums)-1, -1, -1):
            if nums[i] > zeroes:
                zeroes = 0
            elif nums[i] == 0 or zeroes:
                zeroes += 1

        return False if zeroes else True