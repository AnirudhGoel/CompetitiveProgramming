# 239. Sliding Window Maximum

# Solution 1 (My Approach): Use a segment tree - Not fast enough, gives TLE
from math import log2

class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        
        if log2(len(nums)) % 1 == 0:
            # if length of array is a power of 2
            self.tree = [None] * (2 * len(nums) - 1)
        else:
            # if length of array is not a power of 2, we take next power of 2
            self.tree = [None] * (2 ** (int(log2(len(nums))) + 1) * 2 - 1)
        
        self.create_tree(nums, self.tree, 0, len(nums) - 1, 0)
    
    def create_tree(self, nums, seg_tree, l, r, pos):
        if l == r:
            seg_tree[pos] = nums[l]
            return
        
        mid = (l + r) // 2
        self.create_tree(nums, seg_tree, l, mid, 2*pos + 1)
        self.create_tree(nums, seg_tree, mid + 1, r, 2*pos + 2)
        
        seg_tree[pos] = max(seg_tree[2*pos + 1], seg_tree[2*pos + 2])
    
    def get_max_in_seg(self, node_l, node_r, query_l, query_r, pos):
        # node_l and node_r are the left and right indexes of the range represented by the current node
        if query_l <= node_l and query_r >= node_r:
            return self.tree[pos]
        
        if node_r < query_l or node_l > query_r:
            return float("-inf")
        
        mid = (node_l + node_r) // 2
        
        return max(self.get_max_in_seg(node_l, mid, query_l, query_r, 2*pos+1), self.get_max_in_seg(mid+1, node_r, query_l, query_r, 2*pos+2))
        

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        tree = SegmentTree(nums)
        window = list()
        
        for i in range(len(nums) - k + 1):
            window.append(tree.get_max_in_seg(0, len(nums)-1, i, i+k-1, 0))
        
        return window


# Solution 2: Dynamic Programming
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = list()
        i = 0
        curr_max = float("-inf")

        for num in nums:
            left.append(max(curr_max, num))
            curr_max = left[i]

            if (i + 1) % k == 0:
                curr_max = float("-inf")

            i += 1


        extras = len(nums) % k
        right = list()
        nums.reverse()
        curr_max = float("-inf")
        i = 0

        while i < extras:
            right.append(max(curr_max, nums[i]))
            curr_max = right[i]
            i += 1


        curr_max = float("-inf")
        for num in nums[extras:]:
            right.append(max(curr_max, nums[i]))
            curr_max = right[i]

            if (i - extras + 1) % k == 0:
                curr_max = float("-inf")

            i += 1

        right.reverse()

        max_window = list()

        for i in range(len(nums) - k + 1):
            max_window.append(max(right[i], left[i+k-1]))

        return max_window


# Solution 3: Using Deque (fastest) 95.96%
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        res = list()

        deq.append(0)

        for i in range(len(nums)):
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()

            deq.append(i)

            if i - k + 1 > deq[0]:
                deq.popleft()

            if i < k - 1:
                continue

            res.append(nums[deq[0]])

        return res