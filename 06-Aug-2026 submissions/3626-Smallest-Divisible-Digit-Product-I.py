# ────────────────────────────────────────────────────────────
# Problem   : 3345. Smallest Divisible Digit Product I
# URL       : https://leetcode.com/problems/smallest-divisible-digit-product-i/
# Difficulty: Easy
# Tags      : Math, Enumeration
#
# Runtime   : 0 ms
# Memory    : 19.4 MB
# Language  : Python3
# Submitted : 2026-08-06T17:42:06.507Z
#
# Examples
# ────────
# Example 1:
#
# Input: n = 10, t = 2
#
# Output: 10
#
# Explanation:
#
# The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.
#
# Example 2:
#
# Input: n = 15, t = 3
#
# Output: 16
#
# Explanation:
#
# The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= n <= 100
#
# • 1 <= t <= 10
#
# ────────────────────────────────────────────────────────────

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        for i in range(n, 101):
            ans = 1
            num = i
            while num > 0:
                digit = num % 10
                ans = ans * digit
                num = num // 10
            
            if ans % t == 0:
                return i