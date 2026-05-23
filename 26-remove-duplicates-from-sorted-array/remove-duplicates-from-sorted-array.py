class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        unique = 1
        num_len = len(nums)
        while j <= num_len-1:
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
                j += 1
                unique += 1

        return unique
        