class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        l = len(flowerbed)
        if (l == 1):
            if flowerbed[0] == 0 and n == 1:
                return True
            elif flowerbed[0] == 1 and n == 1:
                return False
            elif flowerbed[0] == 1 and n == 0:
                return True
            elif flowerbed[0] == 0 and n == 0:
                return True
            else:
                return False

        for i in range(l):
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif i == l - 1 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1

            else:
                continue

        if n <= 0:
            return True
        else:
            return False
