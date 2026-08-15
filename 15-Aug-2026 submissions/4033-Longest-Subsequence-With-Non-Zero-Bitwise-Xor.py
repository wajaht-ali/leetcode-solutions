# ────────────────────────────────────────────────────────────
# Problem   : 3702. Longest Subsequence With Non-Zero Bitwise XOR
# URL       : https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/
# Difficulty: Medium
# Tags      : Array, Bit Manipulation
#
# Runtime   : 35 ms
# Memory    : 33.1 MB
# Language  : Python3
# Submitted : 2026-08-15T15:54:40.736Z
#
# Examples
# ────────
# Example 1:
#
# Input: nums = [1,2,3]
#
# Output: 2
#
# Explanation:
#
# One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.
#
# Example 2:
#
# Input: nums = [2,3,4]
#
# Output: 3
#
# Explanation:
#
# The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= nums.length <= 10^5
#
# • 0 <= nums[i] <= 10^9
#
# ────────────────────────────────────────────────────────────

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)

        xor = 0
        cnt0 = 0
        for x in nums:
            xor ^= x
            if x == 0:
                cnt0 += 1
        if xor != 0:
            return n
        if cnt0 == n:
            return 0
        return n - 1