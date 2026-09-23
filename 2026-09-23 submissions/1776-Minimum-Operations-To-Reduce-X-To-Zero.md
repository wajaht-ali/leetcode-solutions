# [1658. Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge&logo=leetcode)
![Language](https://img.shields.io/badge/Language-Python3-3776AB?style=for-the-badge&logo=python)
![Runtime](https://img.shields.io/badge/Runtime-46_ms-blue?style=for-the-badge)
![Memory](https://img.shields.io/badge/Memory-31.2_MB-purple?style=for-the-badge)
---

## 📋 Problem Description

You are given an integer array `nums` and an integer `x`. In one operation, you can either remove the leftmost or the rightmost element from the array `nums` and subtract its value from `x`. Note that this **modifies** the array for future operations.

Return *the **minimum number** of operations to reduce *`x` *to **exactly*** `0` *if it is possible**, otherwise, return *`-1`.
---

## 📝 Examples

> Example 1:
> 
> ```
> Input: nums = [1,1,4,2,3], x = 5
> Output: 2
> Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
> ```

> Example 2:
> 
> ```
> Input: nums = [5,6,7,8,9], x = 4
> Output: -1
> ```

> Example 3:
> 
> ```
> Input: nums = [3,2,20,1,1,3], x = 10
> Output: 5
> Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
> ```
> 
> **Constraints:**
> 
> - `1 <= nums.length <= 10^5`
> 
> - `1 <= nums[i] <= 10^4`
> 
> - `1 <= x <= 10^9`

---

## 🏷️ Topic Tags

`Array`  `Hash Table`  `Binary Search`  `Sliding Window`  `Prefix Sum`
---

## 💡 Solution

| Metric | Value |
|:-------|:------|
| **Language** | Python3 |
| **Runtime** | 46 ms |
| **Memory** | 31.2 MB |
| **Submitted** | 2026-09-23T10:50:23.203Z |

```python
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x

        if target < 0:
            return -1

        if target == 0:
            return len(nums)

        left = 0
        curr_sum = 0
        max_len = -1

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        return -1 if max_len == -1 else len(nums) - max_len
```

---

<div align="center">

*Synced by [LeetSync](https://github.com) — LeetCode to GitHub bridge*

</div>
