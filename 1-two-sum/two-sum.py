# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range (len(nums)):
#             for j in range (i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
        


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        i = 0
        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in d):
                j = d[complement]
                if i != j:
                    return [i,j]
