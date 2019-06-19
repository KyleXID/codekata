# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/


def longestPalindrome(self, s):

    if len(s) <= 1:
        return s

    maxstr = s[0]

    for i in range(len(s)-1):
        subs = s[i]

        for j in range(i+1, len(s)):
            subs += s[j]

            if subs == subs[::-1]:
                if len(maxstr) <= len(subs):
                    maxstr = subs

    return maxstr

# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: "cbbd"
# Output: "bb"

def longestPalindrome(self, s):  # 다른 방법
    """
    :type s: str
    :rtype: str
    """
    # Return if string is empty
    if not s: return s

    res = ""
    for i in range(len(s)):
        j = i + 1
        # While j is less than length of string
        # AND res is *not* longer than substring s[i:]
        while j <= len(s) and len(res) <= len(s[i:]):
            # If substring s[i:j] is a palindrome
            # AND substring is longer than res
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                res = s[i:j]
            j += 1

    return res
