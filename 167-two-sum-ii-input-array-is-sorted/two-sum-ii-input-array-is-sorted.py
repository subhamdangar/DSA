class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 1
        j = len(numbers)
        while(i<j):
            output = numbers[i-1] + numbers[j-1]
            if output == target:
                return [i,j]
            elif output < target:
                i += 1
            else:
                j -= 1
