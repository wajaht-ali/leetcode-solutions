# ────────────────────────────────────────────────────────────
# Problem   : 1358. Number of Substrings Containing All Three Characters
# URL       : https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# Difficulty: Medium
# Tags      : Hash Table, String, Sliding Window
#
# Runtime   : 107 ms
# Memory    : 19.4 MB
# Language  : Python3
# Submitted : 2026-06-30T05:22:03.133Z
#
# Examples
# ────────
# Example 1:
#
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
#
# Example 2:
#
# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
#
# Example 3:
#
# Input: s = "abc"
# Output: 1
#
# Constraints
# ───────────
# Constraints:
#
# • 3 <= s.length <= 5 x 10^4
#
# • s only consists of a, b or c characters.
#
# ────────────────────────────────────────────────────────────

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        ans = 0

        freq = {
            'a': 0,
            'b': 0,
            'c': 0
        }

        for right in range(len(s)):

            freq[s[right]] += 1

            while (
                freq['a'] > 0 and
                freq['b'] > 0 and
                freq['c'] > 0
            ):

                ans += len(s) - right

                freq[s[left]] -= 1
                left += 1

        return ans
