# ────────────────────────────────────────────────────────────
# Problem   : 1290. Convert Binary Number in a Linked List to Integer
# URL       : https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Difficulty: Easy
# Tags      : Linked List, Math
#
# Runtime   : 0 ms
# Memory    : 19.3 MB
# Language  : Python3
# Submitted : 2026-06-30T06:57:33.996Z
#
# Examples
# ────────
# Example 1:
#
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
#
# Example 2:
#
# Input: head = [0]
# Output: 0
#
# Constraints
# ───────────
# Constraints:
#
# • The Linked List is not empty.
#
# • Number of nodes will not exceed 30.
#
# • Each node's value is either 0 or 1.
#
# ────────────────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr = head
        arr = []
        ans = 0

        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        n = len(arr)-1
        for num in arr:
            ans = ans + (num * (2 ** n))
            n = n - 1

        return ans