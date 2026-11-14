class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums = sorted(nums)
        i = 0
        j = 1
        n = len(nums)
        while (j < n):
            if nums[i] == nums[j]:
                j += 1
                return True
            else:
                i += 1
                j += 1

        return False