# ────────────────────────────────────────────────────────────
# Problem   : 3867. Sum of GCD of Formed Pairs
# URL       : https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/
# Difficulty: Medium
# Tags      : Array, Math, Two Pointers, Sorting, Simulation, Number Theory
#
# Runtime   : 179 ms
# Memory    : 33.6 MB
# Language  : Python3
# Submitted : 2026-07-16T09:19:59.734Z
#
# Examples
# ────────
# Example 1:
#
# Input: nums = [2,6,4]
#
# Output: 2
#
# Explanation:
#
# Construct prefixGcd:
#
# i
# nums[i]
# mxi
# prefixGcd[i]
#
# 0
# 2
# 2
# 2
#
# 1
# 6
# 6
# 6
#
# 2
# 4
# 6
# 2
#
# prefixGcd = [2, 6, 2]. After sorting, it forms [2, 2, 6].
#
# Pair the smallest and largest elements: gcd(2, 6) = 2. The remaining middle element 2 is ignored. Thus, the sum is 2.
#
# Example 2:
#
# Input: nums = [3,6,2,8]
#
# Output: 5
#
# Explanation:
#
# Construct prefixGcd:
#
# i
# nums[i]
# mxi
# prefixGcd[i]
#
# 0
# 3
# 3
# 3
#
# 1
# 6
# 6
# 6
#
# 2
# 2
# 6
# 2
#
# 3
# 8
# 8
# 8
#
# prefixGcd = [3, 6, 2, 8]. After sorting, it forms [2, 3, 6, 8].
#
# Form pairs: gcd(2, 8) = 2 and gcd(3, 6) = 3. Thus, the sum is 2 + 3 = 5.
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= n == nums.length <= 10^5
#
# • 1 <= nums[i] <= 10^​​​​​​​9
#
# ────────────────────────────────────────────────────────────

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = 0
        prefixGcd = []

        for num in nums:
            mx = max(num, mx)
            prefixGcd.append(gcd(num, mx))
        
        arr = sorted(prefixGcd)

        i = 0
        j = len(arr)-1
        sm = 0

        while i < j:
            pair = gcd(arr[i], arr[j])
            sm = sm + pair
            i += 1
            j -= 1
        
        return sm
