class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(1,len(numbers)+1):
            d[numbers[i-1]] = i

        i = 1
        for i in range(1,len(numbers)+1):
            complement = target - numbers[i-1]
            if (complement in d):
                j = d[complement]
                if i != j:
                    return [i,j]
