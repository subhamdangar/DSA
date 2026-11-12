class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums = sorted(nums)
        lst = []
        for i in range(0, n-2):
            if(i>0 and nums[i] == nums[i-1]):
                continue
            left = i+1
            right = n-1
            sum = (-1)*nums[i]

            while (left < right):
                s = nums[left] + nums[right]
                if (s == sum):
                    lst.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while((left < n) and (nums[left] == nums[left-1])):
                        left += 1
                    while((right > 0) and (nums[right] == nums[right+1])):
                        right -= 1
                elif (s < sum):
                    left += 1
                else:
                    right -= 1
        return lst

