# [2839. Check if Strings Can be Made Equal With Operations I](https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/)

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge&logo=leetcode)
![Language](https://img.shields.io/badge/Language-Python3-3776AB?style=for-the-badge&logo=python)
![Runtime](https://img.shields.io/badge/Runtime-0_ms-blue?style=for-the-badge)
![Memory](https://img.shields.io/badge/Memory-19.3_MB-purple?style=for-the-badge)
---

## 📋 Problem Description

You are given two strings `s1` and `s2`, both of length `4`, consisting of **lowercase** English letters.

You can apply the following operation on any of the two strings **any** number of times:

- Choose any two indices `i` and `j` such that `j - i = 2`, then **swap** the two characters at those indices in the string.

Return `true`* if you can make the strings *`s1`* and *`s2`* equal, and *`false`* otherwise*.
---

## 📝 Examples

> Example 1:
> 
> ```
> Input: s1 = "abcd", s2 = "cdab"
> Output: true
> Explanation: We can do the following operations on s1:
> - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
> - Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.
> ```

> Example 2:
> 
> ```
> Input: s1 = "abcd", s2 = "dacb"
> Output: false
> Explanation: It is not possible to make the two strings equal.
> ```
> 
> **Constraints:**
> 
> - `s1.length == s2.length == 4`
> 
> - `s1` and `s2` consist only of lowercase English letters.

---

## 🏷️ Topic Tags

`String`
---

## 💡 Solution

| Metric | Value |
|:-------|:------|
| **Language** | Python3 |
| **Runtime** | 0 ms |
| **Memory** | 19.3 MB |
| **Submitted** | 2026-09-10T11:24:18.972Z |

```python
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        elif (s1[0] == s2[2] and s1[2] == s2[0] and s1[1] == s2[3] and s1[3] == s2[1]):
            return True

        elif (s1[0] == s2[0] and s1[2] == s2[2] and s1[1] == s2[3] and s1[3] == s2[1]):
            return True

        elif (s1[1] == s2[1] and s1[3] == s2[3] and s1[0] == s2[2] and s1[2] == s2[0]):
            return True

        return False
```

---

<div align="center">

*Synced by [LeetSync](https://github.com) — LeetCode to GitHub bridge*

</div>
