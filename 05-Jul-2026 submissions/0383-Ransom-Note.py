# ────────────────────────────────────────────────────────────
# Problem   : 0383. Ransom Note
# URL       : https://leetcode.com/problems/ransom-note/
# Difficulty: Easy
# Tags      : Hash Table, String, Counting
#
# Runtime   : 23 ms
# Memory    : 19.6 MB
# Language  : Python3
# Submitted : 2026-07-05T10:33:49.219Z
#
# Examples
# ────────
# Example 1:
#
# Input: ransomNote = "a", magazine = "b"
# Output: false
#
# Example 2:
#
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
#
# Example 3:
#
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= ransomNote.length, magazine.length <= 10^5
#
# • ransomNote and magazine consist of lowercase English letters.
#
# ────────────────────────────────────────────────────────────

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        freq = {}

        for ch in magazine:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in ransomNote:
            if freq.get(ch, 0) == 0:
                return False
            freq[ch] -= 1

        return True