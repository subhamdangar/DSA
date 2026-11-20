class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)

        count = {}
        for i in range(1,n+1):
            count[i] = 0

        for num in nums:
            count[num] += 1

        res = []
        for i,j in count.items():
            if j == 0:
                res.append(i)

        return res
                