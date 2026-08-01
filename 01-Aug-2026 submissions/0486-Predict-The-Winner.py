# ────────────────────────────────────────────────────────────
# Problem   : 0486. Predict the Winner
# URL       : https://leetcode.com/problems/predict-the-winner/
# Difficulty: Medium
# Tags      : Array, Math, Dynamic Programming, Recursion, Game Theory
#
# Runtime   : 1624 ms
# Memory    : 18.8 MB
# Language  : Python3
# Submitted : 2026-08-01T19:03:28.390Z
#
# Examples
# ────────
# Example 1:
#
# Input: nums = [1,5,2]
# Output: false
# Explanation: Initially, player 1 can choose between 1 and 2.
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
# Hence, player 1 will never be the winner and you need to return false.
#
# Example 2:
#
# Input: nums = [1,5,233,7]
# Output: true
# Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= nums.length <= 20
#
# • 0 <= nums[i] <= 10^7
#
# ────────────────────────────────────────────────────────────

from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def dp(i, j):
            if i == j:
                return nums[i]

            pick_left = nums[i] - dp(i + 1, j)
            pick_right = nums[j] - dp(i, j - 1)

            return max(pick_left, pick_right)

        return dp(0, len(nums) - 1) >= 0