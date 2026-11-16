class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n = len(nums)
        max = float('-inf')
        min = float('inf')
        for i in range(n):
            if nums[i] > max :
                max = nums[i]
            if nums[i] < min:
                min = nums[i]
        
        for i in range(n):
            if nums[i] != max and nums[i] != min:
                return nums[i]
        return -1

        