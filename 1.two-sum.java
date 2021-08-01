/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i=0 ; i<nums.length-1 ; i++){
            for (int j=i+1; j<nums.length; j++){
                if (nums[i] + nums[j] == target){
                    int[] idx = {i,j};
                    return idx;
                }
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
// @lc code=end

