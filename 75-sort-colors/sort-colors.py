class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        y = 0
        z = 0
        for i in nums:
            if i == 0:
                x += 1
            elif i == 1:
                y += 1
            else:
                z += 1

        nums[:] = ([0]*x) + ([1]*y) + ([2]*z)