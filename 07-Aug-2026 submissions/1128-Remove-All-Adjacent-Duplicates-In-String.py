# ────────────────────────────────────────────────────────────
# Problem   : 1047. Remove All Adjacent Duplicates In String
# URL       : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Difficulty: Easy
# Tags      : String, Stack
#
# Runtime   : 25 ms
# Memory    : 20.1 MB
# Language  : Python3
# Submitted : 2026-08-07T06:19:57.150Z
#
# Examples
# ────────
# Example 1:
#
# Input: s = "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
#
# Example 2:
#
# Input: s = "azxxzy"
# Output: "ay"
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= s.length <= 10^5
#
# • s consists of lowercase English letters.
#
# ────────────────────────────────────────────────────────────

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []

        for ch in s:
            if len(stk) == 0:
                stk.append(ch)
            else:
                if stk[-1] == ch:
                    stk.pop()
                else:
                    stk.append(ch)
        
        return "".join(stk)