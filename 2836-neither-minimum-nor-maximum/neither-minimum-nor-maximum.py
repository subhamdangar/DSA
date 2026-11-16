class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n = len(nums)
        max_elt = float('-inf')
        min_elt = float('inf')
        for i in range(n):
            if nums[i] > max_elt :
                max_elt = nums[i]
            if nums[i] < min_elt:
                min_elt = nums[i]
        
        for i in range(n):
            if nums[i] != max_elt and nums[i] != min_elt:
                return nums[i]
        return -1

        