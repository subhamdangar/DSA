# TC = O(n)
# SC = O(n) 

# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         pos = []
#         neg = []
#         n = len(nums)
#         for i in range(n):
#             if nums[i] >= 0:
#                 pos.append(nums[i])
#             else:
#                 neg.append(nums[i])


#         if (len(pos) == 0):
#             for i in range(n):
#                 nums[i] = nums[i] ** 2
#             return nums[::-1]
#         elif (len(neg) == 0):
#             for i in range(n):
#                 nums[i] = nums[i] ** 2
#             return nums
#         else:
#             # Merge two sorted array
#             pos = [x**2 for x in pos]
#             neg = [x**2 for x in neg]
#             neg = neg[::-1]
#             i = 0
#             j = 0
#             res = []
#             while(i<len(pos) and j <len(neg)):
#                 if (pos[i] <= neg[j]):
#                     res.append(pos[i])
#                     i += 1

#                 else:
#                     res.append(neg[j])
#                     j += 1

#             while (j<len(neg)):
#                 res.append(neg[j])
#                 j += 1
#             while (i<len(pos)):
#                 res.append(pos[i])
#                 i += 1
#             return res


        


# TC = O(n)
# SC = O(1) --> Ignoring the size of res as it is required output array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = n-1
        res = [0]*n
        while i<=j:
            if (nums[i]**2 > nums[j]**2):
                res[n-1] = nums[i]**2
                n = n-1
                i = i+1
            else:
                res[n-1] = nums[j]**2
                n = n-1
                j = j-1

        return res