class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            if count == 0:
                count = 1
                elt = nums[i]
            elif (elt == nums[i]):
                count += 1
            else:
                count -= 1

        elt_count = 0
        for i in range(n):
            if nums[i] == elt:
                elt_count += 1
        if elt_count > (n//2):
            return elt
