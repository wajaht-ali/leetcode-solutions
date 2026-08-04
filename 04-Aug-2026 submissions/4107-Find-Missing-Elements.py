# ────────────────────────────────────────────────────────────
# Problem   : 3731. Find Missing Elements
# URL       : https://leetcode.com/problems/find-missing-elements/
# Difficulty: Easy
# Tags      : Array, Hash Table, Sorting
#
# Runtime   : 3 ms
# Memory    : 19.3 MB
# Language  : Python3
# Submitted : 2026-08-04T15:45:56.398Z
#
# Examples
# ────────
# Example 1:
#
# Input: nums = [1,4,2,5]
#
# Output: [3]
#
# Explanation:
#
# The smallest integer is 1 and the largest is 5, so the full range should be [1,2,3,4,5]. Among these, only 3 is missing.
#
# Example 2:
#
# Input: nums = [7,8,6,9]
#
# Output: []
#
# Explanation:
#
# The smallest integer is 6 and the largest is 9, so the full range is [6,7,8,9]. All integers are already present, so no integer is missing.
#
# Example 3:
#
# Input: nums = [5,1]
#
# Output: [2,3,4]
#
# Explanation:
#
# The smallest integer is 1 and the largest is 5, so the full range should be [1,2,3,4,5]. The missing integers are 2, 3, and 4.
#
# Constraints
# ───────────
# Constraints:
#
# • 2 <= nums.length <= 100
#
# • 1 <= nums[i] <= 100
#
# ────────────────────────────────────────────────────────────

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        arr = []
        curr = sorted(nums)

        for i in range(len(curr)-1):
            c1 = curr[i]
            c2 = curr[i + 1] - 1
            if c1 != c2:
                while c1 < c2:
                    arr.append(c1 + 1)
                    c1 = c1 + 1
        return arr
