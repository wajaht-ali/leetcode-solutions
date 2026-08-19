# ────────────────────────────────────────────────────────────
# Problem   : 1512. Number of Good Pairs
# URL       : https://leetcode.com/problems/number-of-good-pairs/
# Difficulty: Easy
# Tags      : Array, Hash Table, Math, Counting
#
# Runtime   : 3 ms
# Memory    : 19.1 MB
# Language  : Python3
# Submitted : 2026-08-19T16:49:00.737Z
#
# Examples
# ────────
# Example 1:
#
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
#
# Example 2:
#
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
#
# Example 3:
#
# Input: nums = [1,2,3]
# Output: 0
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= nums.length <= 100
#
# • 1 <= nums[i] <= 100
#
# ────────────────────────────────────────────────────────────

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    pair += 1
        
        return pair