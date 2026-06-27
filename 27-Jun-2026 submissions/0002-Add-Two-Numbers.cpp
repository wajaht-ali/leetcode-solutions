/*
 * Problem   : 0002. Add Two Numbers
 * URL       : https://leetcode.com/problems/add-two-numbers/
 * Difficulty: Medium
 * Tags      : Linked List, Math, Recursion
 *
 * Runtime   : 0 ms
 * Memory    : 77 MB
 * Language  : C++
 * Submitted : 2026-06-27T10:47:10.572Z
 *
 * Examples
 * ────────
 * Example 1:
 *
 * Input: l1 = [2,4,3], l2 = [5,6,4]
 * Output: [7,0,8]
 * Explanation: 342 + 465 = 807.
 *
 * Example 2:
 *
 * Input: l1 = [0], l2 = [0]
 * Output: [0]
 *
 * Example 3:
 *
 * Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
 * Output: [8,9,9,9,0,0,0,1]
 *
 * Constraints
 * ───────────
 * Constraints:
 *
 * • The number of nodes in each linked list is in the range [1, 100].
 *
 * • 0 <= Node.val <= 9
 *
 * • It is guaranteed that the list represents a number that does not have leading zeros.
 *
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode dummy(0);
    ListNode* curr = &dummy;
    int carry = 0;

    while(l1 || l2 || carry) {
        int v1 = l1 ? l1->val : 0;
        int v2 = l2 ? l2->val : 0;

        int total = v1 + v2 + carry;
        carry = total / 10;

        curr->next = new ListNode(total % 10);
        curr = curr->next;

        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }
    return dummy.next;
    }
};