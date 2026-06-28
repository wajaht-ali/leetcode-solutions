# ────────────────────────────────────────────────────────────
# Problem   : 1846. Maximum Element After Decreasing and Rearranging
# URL       : https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
# Difficulty: Medium
# Tags      : Array, Greedy, Sorting
#
# Runtime   : 17 ms
# Memory    : 28.5 MB
# Language  : Python3
# Submitted : 2026-06-28T09:51:04.571Z
#
# Examples
# ────────
# Example 1:
#
# Input: arr = [2,2,1,2,1]
# Output: 2
# Explanation:
# We can satisfy the conditions by rearranging arr so it becomes [1,2,2,2,1].
# The largest element in arr is 2.
#
# Example 2:
#
# Input: arr = [100,1,1000]
# Output: 3
# Explanation:
# One possible way to satisfy the conditions is by doing the following:
# 1. Rearrange arr so it becomes [1,100,1000].
# 2. Decrease the value of the second element to 2.
# 3. Decrease the value of the third element to 3.
# Now arr = [1,2,3], which satisfies the conditions.
# The largest element in arr is 3.
#
# Example 3:
#
# Input: arr = [1,2,3,4,5]
# Output: 5
# Explanation: The array already satisfies the conditions, and the largest element is 5.
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= arr.length <= 10^5
#
# • 1 <= arr[i] <= 10^9
#
# ────────────────────────────────────────────────────────────

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        prev = 0
        for n in arr:
            prev = min(prev + 1, n)
        return prev