# ────────────────────────────────────────────────────────────
# Problem   : 0402. Remove K Digits
# URL       : https://leetcode.com/problems/remove-k-digits/
# Difficulty: Medium
# Tags      : String, Stack, Greedy, Monotonic Stack
#
# Runtime   : 21 ms
# Memory    : 20.5 MB
# Language  : Python3
# Submitted : 2026-08-07T06:44:42.525Z
#
# Examples
# ────────
# Example 1:
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
#
# Example 2:
#
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
#
# Example 3:
#
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= k <= num.length <= 10^5
#
# • num consists of only digits.
#
# • num does not have any leading zeros except for the zero itself.
#
# ────────────────────────────────────────────────────────────

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remaining_digits = len(num) - k
      
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
      
        result = ''.join(stack[:remaining_digits]).lstrip('0')
        return result if result else '0'