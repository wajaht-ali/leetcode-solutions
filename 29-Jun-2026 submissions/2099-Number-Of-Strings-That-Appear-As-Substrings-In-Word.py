# ────────────────────────────────────────────────────────────
# Problem   : 1967. Number of Strings That Appear as Substrings in Word
# URL       : https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
# Difficulty: Easy
# Tags      : Array, String
#
# Runtime   : 0 ms
# Memory    : 19.2 MB
# Language  : Python3
# Submitted : 2026-06-29T10:38:01.967Z
#
# Examples
# ────────
# Example 1:
#
# Input: patterns = ["a","abc","bc","d"], word = "abc"
# Output: 3
# Explanation:
# - "a" appears as a substring in "abc".
# - "abc" appears as a substring in "abc".
# - "bc" appears as a substring in "abc".
# - "d" does not appear as a substring in "abc".
# 3 of the strings in patterns appear as a substring in word.
#
# Example 2:
#
# Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
# Output: 2
# Explanation:
# - "a" appears as a substring in "aaaaabbbbb".
# - "b" appears as a substring in "aaaaabbbbb".
# - "c" does not appear as a substring in "aaaaabbbbb".
# 2 of the strings in patterns appear as a substring in word.
#
# Example 3:
#
# Input: patterns = ["a","a","a"], word = "ab"
# Output: 3
# Explanation: Each of the patterns appears as a substring in word "ab".
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= patterns.length <= 100
#
# • 1 <= patterns[i].length <= 100
#
# • 1 <= word.length <= 100
#
# • patterns[i] and word consist of lowercase English letters.
#
# ────────────────────────────────────────────────────────────

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt = 0

        for s in patterns:
            if s in word:
                cnt += 1
        
        return cnt