class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()

        left = 0
        max_length = 0

        for right in range(len(s)):

            # If duplicate exists, shrink window
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add current character
            char_set.add(s[right])

            # Update maximum length
            max_length = max(max_length, right - left + 1)

        return max_length