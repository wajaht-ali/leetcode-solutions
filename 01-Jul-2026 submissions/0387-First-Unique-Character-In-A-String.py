# ────────────────────────────────────────────────────────────
# Problem   : 0387. First Unique Character in a String
# URL       : https://leetcode.com/problems/first-unique-character-in-a-string/
# Difficulty: Easy
# Tags      : Hash Table, String, Queue, Counting
#
# Runtime   : 71 ms
# Memory    : 19.5 MB
# Language  : Python3
# Submitted : 2026-07-01T17:27:26.470Z
#
# Examples
# ────────
# Example 1:
#
# Input: s = "leetcode"
#
# Output: 0
#
# Explanation:
#
# The character 'l' at index 0 is the first character that does not occur at any other index.
#
# Example 2:
#
# Input: s = "loveleetcode"
#
# Output: 2
#
# Example 3:
#
# Input: s = "aabb"
#
# Output: -1
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= s.length <= 10^5
#
# • s consists of only lowercase English letters.
#
# ────────────────────────────────────────────────────────────

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1