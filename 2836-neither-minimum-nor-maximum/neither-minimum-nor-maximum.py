class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        a = nums[0]
        b = nums[1]
        c = nums[2]

        lst = [a,b,c]
        lst.sort()
        ans = lst[1]
        return ans
        