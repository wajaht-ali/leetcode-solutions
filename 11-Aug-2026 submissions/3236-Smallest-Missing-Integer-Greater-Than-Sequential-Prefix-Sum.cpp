/*
 * Problem   : 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
 * URL       : https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
 * Difficulty: Easy
 * Tags      : Array, Hash Table, Sorting
 *
 * Runtime   : 0 ms
 * Memory    : 22.8 MB
 * Language  : C++
 * Submitted : 2026-08-11T18:46:13.427Z
 *
 * Examples
 * ────────
 * Example 1:
 *
 * Input: nums = [1,2,3,2,5]
 * Output: 6
 * Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
 *
 * Example 2:
 *
 * Input: nums = [3,4,5,1,12,14,13]
 * Output: 15
 * Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
 *
 * Constraints
 * ───────────
 * Constraints:
 *
 * • 1 <= nums.length <= 50
 *
 * • 1 <= nums[i] <= 50
 *
 */

class Solution {
public:
    int missingInteger(vector<int>& nums) {
        int sum = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1] + 1)
                sum += nums[i];
            else
                break;
        }

        unordered_set<int> st(nums.begin(), nums.end());

        // Find smallest missing integer >= sum
        while (st.count(sum))
            sum++;

        return sum;
    }
};