class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        n = len(nums)
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

            
        for key, value in freq.items():
            if value > (n//2):
                return key

            