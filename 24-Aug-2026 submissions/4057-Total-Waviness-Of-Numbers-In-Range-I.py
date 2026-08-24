# ────────────────────────────────────────────────────────────
# Problem   : 3751. Total Waviness of Numbers in Range I
# URL       : https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/
# Difficulty: Medium
# Tags      : Math, Dynamic Programming, Enumeration
#
# Runtime   : 757 ms
# Memory    : 19.5 MB
# Language  : Python3
# Submitted : 2026-08-24T08:14:24.842Z
#
# Examples
# ────────
# Example 1:
#
# Input: num1 = 120, num2 = 130
#
# Output: 3
#
# Explanation:
#
# In the range [120, 130]:
#
# • 120: middle digit 2 is a peak, waviness = 1.
#
# • 121: middle digit 2 is a peak, waviness = 1.
#
# • 130: middle digit 3 is a peak, waviness = 1.
#
# • All other numbers in the range have a waviness of 0.
#
# Thus, total waviness is 1 + 1 + 1 = 3.
#
# Example 2:
#
# Input: num1 = 198, num2 = 202
#
# Output: 3
#
# Explanation:
#
# In the range [198, 202]:
#
# • 198: middle digit 9 is a peak, waviness = 1.
#
# • 201: middle digit 0 is a valley, waviness = 1.
#
# • 202: middle digit 0 is a valley, waviness = 1.
#
# • All other numbers in the range have a waviness of 0.
#
# Thus, total waviness is 1 + 1 + 1 = 3.
#
# Example 3:
#
# Input: num1 = 4848, num2 = 4848
#
# Output: 2
#
# Explanation:
#
# Number 4848: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= num1 <= num2 <= 10^5
#
# ────────────────────────────────────────────────────────────

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        peak = 0
        valley = 0
        for num in range(num1, num2+1):

            s = ""
            curr = num
            while curr > 0:
                dig = curr % 10
                s = str(dig) + s
                curr = curr // 10
            
            # return s
            if len(s) < 3:
                continue
            else:
                for ch in range(1, len(s) - 1):
                    if int(s[ch]) > int(s[ch + 1]) and int(s[ch]) > int(s[ch - 1]):
                        peak += 1
                    elif int(s[ch]) < int(s[ch + 1]) and int(s[ch]) < int(s[ch - 1]):
                        valley += 1
                        
        return valley + peak