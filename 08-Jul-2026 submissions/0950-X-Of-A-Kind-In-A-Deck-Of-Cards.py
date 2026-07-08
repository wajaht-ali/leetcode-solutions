# ────────────────────────────────────────────────────────────
# Problem   : 0914. X of a Kind in a Deck of Cards
# URL       : https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
# Difficulty: Easy
# Tags      : Array, Hash Table, Math, Counting, Number Theory
#
# Runtime   : 2 ms
# Memory    : 19.8 MB
# Language  : Python3
# Submitted : 2026-07-08T12:40:28.843Z
#
# Examples
# ────────
# Example 1:
#
# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
#
# Example 2:
#
# Input: deck = [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.
#
# Constraints
# ───────────
# Constraints:
#
# • 1 <= deck.length <= 10^4
#
# • 0 <= deck[i] < 10^4
#
# ────────────────────────────────────────────────────────────

from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck)

        g = reduce(gcd, freq.values())

        return g >= 2