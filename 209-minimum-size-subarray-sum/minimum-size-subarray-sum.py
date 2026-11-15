class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = float('inf')
        i = 0
        j = 0
        n = len(nums)
        curr_subarr_len = 0
        sum = 0

        while(j<n):
            sum = sum + nums[j]
            while(sum >= target):
                curr_subarr_len = j-i+1
                res = min(res, curr_subarr_len)
                sum = sum - nums[i]
                i += 1
            j += 1

        if (res == float('inf')):
            return 0
        else:
            return res

        