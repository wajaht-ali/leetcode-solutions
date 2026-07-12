# ────────────────────────────────────────────────────────────
# Problem   : 1331. Rank Transform of an Array
# URL       : https://leetcode.com/problems/rank-transform-of-an-array/
# Difficulty: Easy
# Tags      : Array, Hash Table, Sorting
#
# Runtime   : 35 ms
# Memory    : 37.7 MB
# Language  : Python3
# Submitted : 2026-07-12T11:46:34.051Z
#
# Examples
# ────────
# Example 1:
#
# Input: arr = [40,10,20,30]
# Output: [4,1,2,3]
# Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
#
# Example 2:
#
# Input: arr = [100,100,100]
# Output: [1,1,1]
# Explanation: Same elements share the same rank.
#
# Example 3:
#
# Input: arr = [37,12,28,9,100,56,80,5,12]
# Output: [5,3,4,2,8,6,7,1,3]
#
# Constraints
# ───────────
# Constraints:
#
# • 0 <= arr.length <= 10^5
#
# • -10^9 <= arr[i] <= 10^9
#
# ────────────────────────────────────────────────────────────

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = sorted(set(arr))

        rank = {}
        for i, num in enumerate(nums):
            rank[num] = i + 1

        return [rank[num] for num in arr]