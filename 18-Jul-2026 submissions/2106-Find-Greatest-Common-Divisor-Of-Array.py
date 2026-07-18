# ────────────────────────────────────────────────────────────
# Problem   : 1979. Find Greatest Common Divisor of Array
# URL       : https://leetcode.com/problems/find-greatest-common-divisor-of-array/
# Difficulty: Easy
# Tags      : Array, Math, Number Theory
#
# Runtime   : 0 ms
# Memory    : 19.3 MB
# Language  : Python3
# Submitted : 2026-07-18T11:26:51.431Z
#
# Examples
# ────────
# Example 1:
#
# Input: nums = [2,5,6,9,10]
# Output: 2
# Explanation:
# The smallest number in nums is 2.
# The largest number in nums is 10.
# The greatest common divisor of 2 and 10 is 2.
#
# Example 2:
#
# Input: nums = [7,5,6,8,3]
# Output: 1
# Explanation:
# The smallest number in nums is 3.
# The largest number in nums is 8.
# The greatest common divisor of 3 and 8 is 1.
#
# Example 3:
#
# Input: nums = [3,3]
# Output: 3
# Explanation:
# The smallest number in nums is 3.
# The largest number in nums is 3.
# The greatest common divisor of 3 and 3 is 3.
#
# Constraints
# ───────────
# Constraints:
#
# • 2 <= nums.length <= 1000
#
# • 1 <= nums[i] <= 1000
#
# ────────────────────────────────────────────────────────────

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        arr = sorted(nums)
        a = arr[0]
        b = arr[len(arr)-1]

        ans = gcd(a, b)
        return ans