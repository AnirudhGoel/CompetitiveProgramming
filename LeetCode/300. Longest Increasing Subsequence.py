# 300. Longest Increasing Subsequence

# Approach 1: TLE due to many extra elements being generated
# For example, [10,9,2,5,3,7,101,18] generates [[18, 7, 3, 2], [101, 7, 3, 2], [18, 7, 5, 2], [101, 7, 5, 2], [18, 9], [101, 9], [18, 9], [101, 9], [18, 10], [101, 10], [18, 10], [101, 10], [18, 10], [101, 10], [18, 10], [101, 10]] on the print statement
# This has lot of repetitive elements such as [101, 10], [18, 10]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sequences = [[nums[-1]]]
        
        for i in range(len(nums) - 2, -1, -1):
            len_sequences = len(sequences)
            individual_seq = False
            for j in range(len_sequences):
                pos = len(sequences[j])
                
                if sequences[j][-1] == nums[i]:
                    continue
                    
                if nums[i] < sequences[j][-1]:
                    sequences[j].append(nums[i])
                    continue
                
                while pos != 0 and nums[i] >= sequences[j][pos-1]:
                    pos -= 1
                
                if pos == 0:
                    if individual_seq:
                        continue
                    else:
                        individual_seq = True
                
                sequences.append(sequences[j][:pos])
                sequences[-1].append(nums[i])
        
        # print(sequences)
        max_seq_len = 1
        
        for seq in sequences:
            max_seq_len = max(max_seq_len, len(seq))
        
        return max_seq_len

# Approach 2: Fuck! This is the approach I thought of at first but didn't think of it clearly enough so discarded it at that time!
# 54% faster
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)