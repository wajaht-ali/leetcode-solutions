# ────────────────────────────────────────────────────────────
# Problem   : 0203. Remove Linked List Elements
# URL       : https://leetcode.com/problems/remove-linked-list-elements/
# Difficulty: Easy
# Tags      : Linked List, Recursion
#
# Runtime   : 0 ms
# Memory    : 22.3 MB
# Language  : Python3
# Submitted : 2026-06-27T10:42:23.792Z
#
# Examples
# ────────
# Example 1:
#
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
#
# Example 2:
#
# Input: head = [], val = 1
# Output: []
#
# Example 3:
#
# Input: head = [7,7,7,7], val = 7
# Output: []
#
# Constraints
# ───────────
# Constraints:
#
# • The number of nodes in the list is in the range [0, 10^4].
#
# • 1 <= Node.val <= 50
#
# • 0 <= val <= 50
#
# ────────────────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        itr = head
        while itr and itr.next:
            if itr.next.val == val:
                itr.next = itr.next.next
            else:
                itr = itr.next
        
        if head.val == val:
            return head.next
        
        return head
        