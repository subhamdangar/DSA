class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        max_elt = float("-inf")
        n = len(nums)
        for i in range(n):
            if nums[i] > max_elt:
                max_elt = nums[i]
                res = i
        return res


        