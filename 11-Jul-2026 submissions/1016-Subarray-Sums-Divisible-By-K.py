# ────────────────────────────────────────────────────────────
# Problem   : 0974. Subarray Sums Divisible by K
# URL       : https://leetcode.com/problems/subarray-sums-divisible-by-k/
# Difficulty: Medium
# Tags      : Array, Hash Table, Prefix Sum
#
# Runtime   : 28 ms
# Memory    : 23.7 MB
# Language  : Python3
# Submitted : 2026-07-11T16:54:35.601Z
#
# Examples
# ────────
# Example 1:
#
# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#
# Example 2:
#
# Input: nums = [5], k = 9
# Output: 0
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= nums.length <= 3 * 10^4
#
# • -10^4 <= nums[i] <= 10^4
#
# • 2 <= k <= 10^4
#
# ────────────────────────────────────────────────────────────

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        prefix = 0
        ans = 0

        for num in nums:
            prefix += num
            rem = prefix % k

            ans += freq.get(rem, 0)
            freq[rem] = freq.get(rem, 0) + 1

        return ans