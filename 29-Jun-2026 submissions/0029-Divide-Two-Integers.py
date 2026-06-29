# ────────────────────────────────────────────────────────────
# Problem   : 0029. Divide Two Integers
# URL       : https://leetcode.com/problems/divide-two-integers/
# Difficulty: Medium
# Tags      : Math, Bit Manipulation
#
# Runtime   : 4 ms
# Memory    : 19.3 MB
# Language  : Python3
# Submitted : 2026-06-29T10:22:22.455Z
#
# Examples
# ────────
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
#
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
#
# Constraints
# ───────────
# Constraints:
#
# • -2^31 <= dividend, divisor <= 2^31 - 1
#
# • divisor != 0
#
# ────────────────────────────────────────────────────────────

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        ans = 0

        while dividend >= divisor:

            shift = 0

            while dividend >= (divisor << (shift + 1)):
                shift += 1

            ans += (1 << shift)
            dividend -= (divisor << shift)

        if negative:
            ans = -ans

        return ans