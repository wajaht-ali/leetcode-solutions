# [3871. Count Commas in Range II](https://leetcode.com/problems/count-commas-in-range-ii/)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge&logo=leetcode)
![Language](https://img.shields.io/badge/Language-Python3-3776AB?style=for-the-badge&logo=python)
![Runtime](https://img.shields.io/badge/Runtime-0_ms-blue?style=for-the-badge)
![Memory](https://img.shields.io/badge/Memory-19.1_MB-purple?style=for-the-badge)
---

## 📋 Problem Description

You are given an integer `n`.

Return the **total** number of commas used when writing all integers from `[1, n]` (inclusive) in **standard** number formatting.

In **standard** formatting:

- A comma is inserted after **every three** digits from the right.

- Numbers with **fewer** than 4 digits contain no commas.
---

## 📝 Examples

> Example 1:
> 
> **Input:** n = 1002
> 
> **Output:** 3
> 
> **Explanation:**
> 
> The numbers `"1,000"`, `"1,001"`, and `"1,002"` each contain one comma, giving a total of 3.

> Example 2:
> 
> **Input:** n = 998
> 
> **Output:** 0
> 
> **Explanation:**
> 
> **​​​​​​​**All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.
> 
> **Constraints:**
> 
> - `1 <= n <= 10^15`

---

## 🏷️ Topic Tags

`Math`
---

## 💡 Solution

| Metric | Value |
|:-------|:------|
| **Language** | Python3 |
| **Runtime** | 0 ms |
| **Memory** | 19.1 MB |
| **Submitted** | 2026-09-09T08:34:40.432Z |

```python
class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        x = 1000

        while x <= n:
            ans += n - x + 1
            x *= 1000

        return ans
```

---

<div align="center">

*Synced by [LeetSync](https://github.com) — LeetCode to GitHub bridge*

</div>
