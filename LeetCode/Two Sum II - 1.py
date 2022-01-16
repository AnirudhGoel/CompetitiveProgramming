class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        total = numbers[l] + numbers[r]
        
        while total != target:
            (l, r) = (l + 1, r) if total < target else (l, r - 1)
            total = numbers[l] + numbers[r]
            
        return [l+1, r+1]