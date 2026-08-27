# [0414. Third Maximum Number](https://leetcode.com/problems/third-maximum-number/)

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge&logo=leetcode)
![Language](https://img.shields.io/badge/Language-Python3-3776AB?style=for-the-badge&logo=python)
![Runtime](https://img.shields.io/badge/Runtime-284_ms-blue?style=for-the-badge)
![Memory](https://img.shields.io/badge/Memory-19.9_MB-purple?style=for-the-badge)
---

## 📋 Problem Description

Given an integer array `nums`, return *the **third distinct maximum** number in this array. If the third maximum does not exist, return the **maximum** number*.
---

## 📝 Examples

> Example 1:
> 
> ```
> Input: nums = [3,2,1]
> Output: 1
> Explanation:
> The first distinct maximum is 3.
> The second distinct maximum is 2.
> The third distinct maximum is 1.
> ```

> Example 2:
> 
> ```
> Input: nums = [1,2]
> Output: 2
> Explanation:
> The first distinct maximum is 2.
> The second distinct maximum is 1.
> The third distinct maximum does not exist, so the maximum (2) is returned instead.
> ```

> Example 3:
> 
> ```
> Input: nums = [2,2,3,1]
> Output: 1
> Explanation:
> The first distinct maximum is 3.
> The second distinct maximum is 2 (both 2's are counted together since they have the same value).
> The third distinct maximum is 1.
> ```
> 
> **Constraints:**
> 
> - `1 <= nums.length <= 10^4`
> 
> - `-2^31 <= nums[i] <= 2^31 - 1`
> 
> **Follow up:** Can you find an `O(n)` solution?

---

## 🏷️ Topic Tags

`Array`  `Sorting`
---

## 💡 Solution

| Metric | Value |
|:-------|:------|
| **Language** | Python3 |
| **Runtime** | 284 ms |
| **Memory** | 19.9 MB |
| **Submitted** | 2026-08-27T15:38:56.325Z |

```python
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        freq = []

        for num in nums:
            if num not in freq:
                freq.append(num)
        
        curr = sorted(freq, reverse=True)
        # return curr
        if len(curr) < 3:
            return curr[0]
        else:
            return curr[2]

```

---

<div align="center">

*Synced by [LeetSync](https://github.com) — LeetCode to GitHub bridge*

</div>
