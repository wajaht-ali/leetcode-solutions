# ────────────────────────────────────────────────────────────
# Problem   : 2357. Make Array Zero by Subtracting Equal Amounts
# URL       : https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
# Difficulty: Easy
# Tags      : Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Simulation
#
# Runtime   : 8 ms
# Memory    : 19.3 MB
# Language  : Python3
# Submitted : 2026-08-16T17:01:44.367Z
#
# Examples
# ────────
# Example 1:
#
# Input: nums = [1,5,0,3,5]
# Output: 3
# Explanation:
# In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
# In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
# In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
#
# Example 2:
#
# Input: nums = [0]
# Output: 0
# Explanation: Each element in nums is already 0 so no operations are needed.
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= nums.length <= 100
#
# • 0 <= nums[i] <= 100
#
# ────────────────────────────────────────────────────────────

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            positive = [x for x in nums if x > 0]

            if not positive:
                return i

            mini = min(positive)

            for j in range(len(nums)):
                if nums[j] > 0:
                    nums[j] -= mini

        return len(nums)