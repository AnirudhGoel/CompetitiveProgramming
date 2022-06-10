# 1014. Best Sightseeing Pair

# Solution 1: Brute Force (n^2)
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        
        for i in range(len(values)):
            for j in range(i+1, len(values)):
                max_score = max(max_score, values[i] + values[j] + i - j)
        
        return max_score

# Solution 2: DP (Thought myself! Yay!)
# O(N) Time and O(1) Space
# Same logic as mine is explained in this - https://leetcode.com/problems/best-sightseeing-pair/discuss/2069838/Python%3A-O(n)-time-O(1)-space
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_left = values[0]
        max_score = 0

        for i in range(1, len(values)):
            max_score = max(max_score, max_left + values[i] - 1)
            max_left = max(max_left - 1, values[i])

        return max_score