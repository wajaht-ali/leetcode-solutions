# ────────────────────────────────────────────────────────────
# Problem   : 3658. GCD of Odd and Even Sums
# URL       : https://leetcode.com/problems/gcd-of-odd-and-even-sums/
# Difficulty: Easy
# Tags      : Math, Number Theory
#
# Runtime   : 0 ms
# Memory    : 19 MB
# Language  : Python3
# Submitted : 2026-07-16T09:00:39.445Z
#
# Examples
# ────────
# Example 1:
#
# Input: n = 4
#
# Output: 4
#
# Explanation:
#
# • Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16
#
# • Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20
#
# Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.
#
# Example 2:
#
# Input: n = 5
#
# Output: 5
#
# Explanation:
#
# • Sum of the first 5 odd numbers sumOdd = 1 + 3 + 5 + 7 + 9 = 25
#
# • Sum of the first 5 even numbers sumEven = 2 + 4 + 6 + 8 + 10 = 30
#
# Hence, GCD(sumOdd, sumEven) = GCD(25, 30) = 5.
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= n <= 10​​​​​​​00
#
# ────────────────────────────────────────────────────────────

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = n * n
        sumEven = n * (n + 1)

        ans = gcd(sumOdd, sumEven)
        return ans