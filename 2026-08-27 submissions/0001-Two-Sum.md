# [0001. Two Sum](https://leetcode.com/problems/two-sum/)

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge&logo=leetcode)
![Language](https://img.shields.io/badge/Language-Python3-3776AB?style=for-the-badge&logo=python)
![Runtime](https://img.shields.io/badge/Runtime-1712_ms-blue?style=for-the-badge)
![Memory](https://img.shields.io/badge/Memory-20_MB-purple?style=for-the-badge)
---

## 📋 Problem Description

You are given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.
---

## 📝 Examples

> Example 1:
> 
> ```
> Input: nums = [2,7,11,15], target = 9
> Output: [0,1]
> Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
> ```

> Example 2:
> 
> ```
> Input: nums = [3,2,4], target = 6
> Output: [1,2]
> ```

> Example 3:
> 
> ```
> Input: nums = [3,3], target = 6
> Output: [0,1]
> ```
> 
> **Constraints:**
> 
> - `2 <= nums.length <= 10^4`
> 
> - `-10^9 <= nums[i] <= 10^9`
> 
> - `-10^9 <= target <= 10^9`
> 
> - **Only one valid answer exists.**
> 
> **Follow-up: **Can you come up with an algorithm that is less than `O(n^2)` time complexity?

---

## 🏷️ Topic Tags

`Array`  `Hash Table`
---

## 💡 Solution

| Metric | Value |
|:-------|:------|
| **Language** | Python3 |
| **Runtime** | 1712 ms |
| **Memory** | 20 MB |
| **Submitted** | 2026-08-27T15:25:33.883Z |

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

---

<div align="center">

*Synced by [LeetSync](https://github.com) — LeetCode to GitHub bridge*

</div>
