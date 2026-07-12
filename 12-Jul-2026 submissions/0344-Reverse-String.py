# ────────────────────────────────────────────────────────────
# Problem   : 0344. Reverse String
# URL       : https://leetcode.com/problems/reverse-string/
# Difficulty: Easy
# Tags      : Two Pointers, String
#
# Runtime   : 0 ms
# Memory    : 23.4 MB
# Language  : Python3
# Submitted : 2026-07-12T11:50:37.638Z
#
# Examples
# ────────
# Example 1:
#
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
# Example 2:
#
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= s.length <= 10^5
#
# • s[i] is a printable ascii character.
#
# ────────────────────────────────────────────────────────────

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1

        while l <= r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        
        return s