# ────────────────────────────────────────────────────────────
# Problem   : 0005. Longest Palindromic Substring
# URL       : https://leetcode.com/problems/longest-palindromic-substring/
# Difficulty: Medium
# Tags      : Two Pointers, String, Dynamic Programming
#
# Runtime   : 259 ms
# Memory    : 19.4 MB
# Language  : Python3
# Submitted : 2026-07-09T07:14:57.702Z
#
# Examples
# ────────
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= s.length <= 1000
#
# • s consist of only digits and English letters.
#
# ────────────────────────────────────────────────────────────

class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(len(s)):

            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1

            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]