# ────────────────────────────────────────────────────────────
# Problem   : 0299. Bulls and Cows
# URL       : https://leetcode.com/problems/bulls-and-cows/
# Difficulty: Medium
# Tags      : Hash Table, String, Counting
#
# Runtime   : 7 ms
# Memory    : 19.4 MB
# Language  : Python3
# Submitted : 2026-07-05T10:19:52.049Z
#
# Examples
# ────────
# Example 1:
#
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
# |
# "7810"
#
# Example 2:
#
# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
# |      or     |
# "0111"        "0111"
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= secret.length, guess.length <= 1000
#
# • secret.length == guess.length
#
# • secret and guess consist of digits only.
#
# ────────────────────────────────────────────────────────────

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        freq = {}

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                freq[secret[i]] = freq.get(secret[i], 0) + 1

        for i in range(len(secret)):
            if secret[i] != guess[i]:
                if freq.get(guess[i], 0) > 0:
                    cows += 1
                    freq[guess[i]] -= 1

        return f"{bulls}A{cows}B"