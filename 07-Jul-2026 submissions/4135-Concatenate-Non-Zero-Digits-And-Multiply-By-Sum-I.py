# ────────────────────────────────────────────────────────────
# Problem   : 3754. Concatenate Non-Zero Digits and Multiply by Sum I
# URL       : https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/
# Difficulty: Easy
# Tags      : Math
#
# Runtime   : 1 ms
# Memory    : 19.2 MB
# Language  : Python3
# Submitted : 2026-07-07T09:03:11.381Z
#
# Examples
# ────────
# Example 1:
#
# Input: n = 10203004
#
# Output: 12340
#
# Explanation:
#
# • The non-zero digits are 1, 2, 3, and 4. Thus, x = 1234.
#
# • The sum of digits is sum = 1 + 2 + 3 + 4 = 10.
#
# • Therefore, the answer is x * sum = 1234 * 10 = 12340.
#
# Example 2:
#
# Input: n = 1000
#
# Output: 1
#
# Explanation:
#
# • The non-zero digit is 1, so x = 1 and sum = 1.
#
# • Therefore, the answer is x * sum = 1 * 1 = 1.
#
# Constraints
# ───────────
# Constraints:
#
# • 0 <= n <= 10^9
#
# ────────────────────────────────────────────────────────────

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # step 1:- get all the non-zero integers
        # step 2:- also create a variable to make their sum
        # step 3:- multiply the new number with its sum
        # step 4:- return ans

        if n == 0:
            return 0
        x = n
        sm = 0
        st = ""

        while x > 0:
            digit = x % 10
            if digit != 0:
                sm += digit
                st += str(digit)
            x //= 10

        rev_str = st[::-1]
        return int(rev_str) * sm
