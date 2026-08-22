# ────────────────────────────────────────────────────────────
# Problem   : 3622. Check Divisibility by Digit Sum and Product
# URL       : https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
# Difficulty: Easy
# Tags      : Math
#
# Runtime   : 0 ms
# Memory    : 19.1 MB
# Language  : Python3
# Submitted : 2026-08-22T07:15:25.576Z
#
# Examples
# ────────
# Example 1:
#
# Input: n = 99
#
# Output: true
#
# Explanation:
#
# Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.
#
# Example 2:
#
# Input: n = 23
#
# Output: false
#
# Explanation:
#
# Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= n <= 10^6
#
# ────────────────────────────────────────────────────────────

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digSum = 0
        digPrd = 1

        num = n
        while num > 0:
            dig = num % 10
            digSum = digSum + dig
            digPrd = digPrd * dig
            num = num // 10
        
        total = digSum + digPrd
        if n % total == 0:
            return True
        else:
            return False