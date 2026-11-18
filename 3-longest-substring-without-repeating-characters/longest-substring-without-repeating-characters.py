class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 0
        max_len = 0
        char_set = set()

        while(j < n):
            while (s[j] in char_set):
                char_set.remove(s[i])
                i += 1

            if (s[j] not in char_set):
                char_set.add(s[j])
            
            max_len = max(max_len, j-i+1)

            j +=1


        return max_len

