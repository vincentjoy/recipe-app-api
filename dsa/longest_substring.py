# Longest substring without repeating characters

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.



def lengthOfLongestSubstring(self, s):
        max_length = 0
        start = 0
        char_index_map = {}

        for index, char in enumerate(s):
            if char_index_map[char]>=start:
                start = char_index_map[char] + 1

            char_index_map[char] = index
            max_length = max(max_length, index - start + 1)

        return max_length