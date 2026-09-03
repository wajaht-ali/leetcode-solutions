# [3875. Construct Uniform Parity Array I](https://leetcode.com/problems/construct-uniform-parity-array-i/)

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge&logo=leetcode)
![Language](https://img.shields.io/badge/Language-Python3-3776AB?style=for-the-badge&logo=python)
![Runtime](https://img.shields.io/badge/Runtime-0_ms-blue?style=for-the-badge)
![Memory](https://img.shields.io/badge/Memory-19.3_MB-purple?style=for-the-badge)
---

## 📋 Problem Description

You are given an array `nums1` of `n` **distinct** integers.

You want to construct another array `nums2` of length `n` such that the elements in `nums2` are either **all odd or all even**.

For each index `i`, you must choose **exactly one** of the following (in any order):

- `nums2[i] = nums1[i]`

- `nums2[i] = nums1[i] - nums1[j]`, for an index `j != i`

Return `true` if it is possible to construct such an array, otherwise, return `false`.
---

## 📝 Examples

> Example 1:
> 
> **Input:** nums1 = [2,3]
> 
> **Output:** true
> 
> **Explanation:**
> 
> - Choose `nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1`.
> 
> - Choose `nums2[1] = nums1[1] = 3`.
> 
> - `nums2 = [-1, 3]`, and both elements are odd. Thus, the answer is `true`​​​​​​​.

> Example 2:
> 
> **Input:** nums1 = [4,6]
> 
> **Output:** true
> 
> **Explanation:**​​​​​​​
> 
> - Choose `nums2[0] = nums1[0] = 4`.
> 
> - Choose `nums2[1] = nums1[1] = 6`.
> 
> - `nums2 = [4, 6]`, and all elements are even. Thus, the answer is `true`.
> 
> **Constraints:**
> 
> - `1 <= n == nums1.length <= 100`
> 
> - `1 <= nums1[i] <= 100`
> 
> - `nums1` consists of distinct integers.

---

## 🏷️ Topic Tags

`Array`  `Math`
---

## 💡 Solution

| Metric | Value |
|:-------|:------|
| **Language** | Python3 |
| **Runtime** | 0 ms |
| **Memory** | 19.3 MB |
| **Submitted** | 2026-09-03T06:16:34.504Z |

```python
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True
```

---

<div align="center">

*Synced by [LeetSync](https://github.com) — LeetCode to GitHub bridge*

</div>
