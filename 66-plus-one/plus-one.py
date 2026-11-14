class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        i = n-1
        while(i >= 0):
            temp = digits[i] + 1
            if temp > 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] = temp
                temp = 0
                break
        
        if temp != 0:
            digits.insert(0,1)

        return digits




        