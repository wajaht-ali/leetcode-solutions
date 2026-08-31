# [2091. Removing Minimum and Maximum From Array](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge&logo=leetcode)
![Language](https://img.shields.io/badge/Language-Python3-3776AB?style=for-the-badge&logo=python)
![Runtime](https://img.shields.io/badge/Runtime-31_ms-blue?style=for-the-badge)
![Memory](https://img.shields.io/badge/Memory-34_MB-purple?style=for-the-badge)
---

## 📋 Problem Description

You are given a **0-indexed** array of **distinct** integers `nums`.

There is an element in `nums` that has the **lowest** value and an element that has the **highest** value. We call them the **minimum** and **maximum** respectively. Your goal is to remove **both** these elements from the array.

A **deletion** is defined as either removing an element from the **front** of the array or removing an element from the **back** of the array.

Return *the **minimum** number of deletions it would take to remove **both** the minimum and maximum element from the array.*
---

## 📝 Examples

> Example 1:
> 
> ```
> Input: nums = [2,10,7,5,4,1,8,6]
> Output: 5
> Explanation:
> The minimum element in the array is nums[5], which is 1.
> The maximum element in the array is nums[1], which is 10.
> We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
> This results in 2 + 3 = 5 deletions, which is the minimum number possible.
> ```

> Example 2:
> 
> ```
> Input: nums = [0,-4,19,1,8,-2,-3,5]
> Output: 3
> Explanation:
> The minimum element in the array is nums[1], which is -4.
> The maximum element in the array is nums[2], which is 19.
> We can remove both the minimum and maximum by removing 3 elements from the front.
> This results in only 3 deletions, which is the minimum number possible.
> ```

> Example 3:
> 
> ```
> Input: nums = [101]
> Output: 1
> Explanation:
> There is only one element in the array, which makes it both the minimum and maximum element.
> We can remove it with 1 deletion.
> ```
> 
> **Constraints:**
> 
> - `1 <= nums.length <= 10^5`
> 
> - `-10^5 <= nums[i] <= 10^5`
> 
> - The integers in `nums` are **distinct**.

---

## 🏷️ Topic Tags

`Array`  `Greedy`
---

## 💡 Solution

| Metric | Value |
|:-------|:------|
| **Language** | Python3 |
| **Runtime** | 31 ms |
| **Memory** | 34 MB |
| **Submitted** | 2026-08-31T09:41:33.381Z |

```python
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        mini = nums[0]
        maxi = nums[0]
        min_idx = 0
        max_idx = 0

        for k in range(n):
            if nums[k] < mini:
                mini = nums[k]
                min_idx = k

            if nums[k] > maxi:
                maxi = nums[k]
                max_idx = k

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        both_left = right + 1
        both_right = n - left

        min_left_max_right = left + 1 + n - right
        max_left_min_right = right + 1 + n - left

        return min(
            both_left,
            both_right,
            min_left_max_right,
            max_left_min_right
        )
```

---

<div align="center">

*Synced by [LeetSync](https://github.com) — LeetCode to GitHub bridge*

</div>
