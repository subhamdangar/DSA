class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        