# ────────────────────────────────────────────────────────────
# Problem   : 1480. Running Sum of 1d Array
# URL       : https://leetcode.com/problems/running-sum-of-1d-array/
# Difficulty: Easy
# Tags      : Array, Prefix Sum
#
# Runtime   : 0 ms
# Memory    : 19.4 MB
# Language  : Python3
# Submitted : 2026-07-11T16:58:01.073Z
#
# Examples
# ────────
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#
# Example 2:
#
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
#
# Example 3:
#
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= nums.length <= 1000
#
# • -10^6 <= nums[i] <= 10^6
#
# ────────────────────────────────────────────────────────────

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        sm = 0
        for i in nums:
            sm = sm + i
            ans.append(sm)
        return ans