/*
 * Problem   : 2619. Array Prototype Last
 * URL       : https://leetcode.com/problems/array-prototype-last/
 * Difficulty: Easy
 * Tags      : N/A
 *
 * Runtime   : 42 ms
 * Memory    : 54.5 MB
 * Language  : JavaScript
 * Submitted : 2026-06-30T07:21:00.461Z
 *
 * Examples
 * ────────
 * Example 1:
 *
 * Input: nums = [null, {}, 3]
 * Output: 3
 * Explanation: Calling nums.last() should return the last element: 3.
 *
 * Example 2:
 *
 * Input: nums = []
 * Output: -1
 * Explanation: Because there are no elements, return -1.
 *
 * Constraints
 * ───────────
 * Constraints:
 *
 * • arr is a valid JSON array
 *
 * • 0 <= arr.length <= 1000
 *
 */

/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    if (this.length == 0) {
        return -1
    }

    return this[this.length-1]
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */