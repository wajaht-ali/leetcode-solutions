# ────────────────────────────────────────────────────────────
# Problem   : 3014. Minimum Number of Pushes to Type Word I
# URL       : https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/
# Difficulty: Easy
# Tags      : Math, String, Greedy
#
# Runtime   : 0 ms
# Memory    : 19.2 MB
# Language  : Python3
# Submitted : 2026-07-30T13:23:43.998Z
#
# Examples
# ────────
# Example 1:
#
# Input: word = "abcde"
# Output: 5
# Explanation: The remapped keypad given in the image provides the minimum cost.
# "a" -> one push on key 2
# "b" -> one push on key 3
# "c" -> one push on key 4
# "d" -> one push on key 5
# "e" -> one push on key 6
# Total cost is 1 + 1 + 1 + 1 + 1 = 5.
# It can be shown that no other mapping can provide a lower cost.
#
# Example 2:
#
# Input: word = "xycdefghij"
# Output: 12
# Explanation: The remapped keypad given in the image provides the minimum cost.
# "x" -> one push on key 2
# "y" -> two pushes on key 2
# "c" -> one push on key 3
# "d" -> two pushes on key 3
# "e" -> one push on key 4
# "f" -> one push on key 5
# "g" -> one push on key 6
# "h" -> one push on key 7
# "i" -> one push on key 8
# "j" -> one push on key 9
# Total cost is 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = 12.
# It can be shown that no other mapping can provide a lower cost.
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= word.length <= 26
#
# • word consists of lowercase English letters.
#
# • All letters in word are distinct.
#
# ────────────────────────────────────────────────────────────

class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        for i in range(len(word)):
            ans += (i//8)+1
        
        return ans