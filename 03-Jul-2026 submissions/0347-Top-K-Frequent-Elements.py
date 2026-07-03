# ────────────────────────────────────────────────────────────
# Problem   : 0347. Top K Frequent Elements
# URL       : https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium
# Tags      : Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
#
# Runtime   : 7 ms
# Memory    : 22.7 MB
# Language  : Python3
# Submitted : 2026-07-03T18:50:52.857Z
#
# Examples
# ────────
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
#
# Output: [1,2]
#
# Example 2:
#
# Input: nums = [1], k = 1
#
# Output: [1]
#
# Example 3:
#
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
#
# Output: [1,2]
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= nums.length <= 10^5
#
# • -10^4 <= nums[i] <= 10^4
#
# • k is in the range [1, the number of unique elements in the array].
#
# • It is guaranteed that the answer is unique.
#
# ────────────────────────────────────────────────────────────

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sorted_freq = sorted(
        freq.items(),
        key=lambda x: x[1],
        reverse=True)

        ans = []

        for num, count in sorted_freq:
            if k > 0:
                ans.append(num)
                k -= 1

        return ans


