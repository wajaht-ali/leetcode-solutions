# ────────────────────────────────────────────────────────────
# Problem   : 3718. Smallest Missing Multiple of K
# URL       : https://leetcode.com/problems/smallest-missing-multiple-of-k/
# Difficulty: Easy
# Tags      : Array, Hash Table
#
# Runtime   : 0 ms
# Memory    : 19.3 MB
# Language  : Python3
# Submitted : 2026-08-26T09:07:05.882Z
#
# Examples
# ────────
# Example 1:
#
# Input: nums = [8,2,3,4,6], k = 2
#
# Output: 10
#
# Explanation:
#
# The multiples of k = 2 are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from nums is 10.
#
# Example 2:
#
# Input: nums = [1,4,7,10,15], k = 5
#
# Output: 5
#
# Explanation:
#
# The multiples of k = 5 are 5, 10, 15, 20... and the smallest multiple missing from nums is 5.
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= nums.length <= 100
#
# • 1 <= nums[i] <= 100
#
# • 1 <= k <= 100
#
# ────────────────────────────────────────────────────────────

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        arr = sorted(nums)
        
        curr = []
        for num in arr:
            if num < k:
                continue
            else:
                if num % k == 0:
                    curr.append(num)
        
        for i in range(1, 501):
            if i % k == 0 and i not in curr:
                return i
            
