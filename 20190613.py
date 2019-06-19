# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(self, s):
    d = ""
    f = ""
    for i in range(len(s)):
        if s[i] not in f:
            f += s[i]
        else:
            if len(d) < len(f):
                d = f
            f = f[f.index(s[i])+1::] + s[i]

    return max(len(d), len(f))


# 다른 방법
def lengthOfLongestSubstring(self, s):
    dct = {}
    max_so_far = curr_max = start = 0
    for index, i in enumerate(s):
        if i in dct and dct[i] >= start:
            max_so_far = max(max_so_far, curr_max)
            curr_max = index - dct[i]
            start = dct[i] + 1
        else:
            curr_max += 1
        dct[i] = index
    return max(max_so_far, curr_max)


"""
Given a string, find the length of the longest substring
without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring,
             "pwke" is a subsequence and not a substring.
"""
