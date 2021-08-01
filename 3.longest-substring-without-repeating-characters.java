/*
 * @lc app=leetcode id=3 lang=java
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
class Solution {
    String substr;
    String longestStr = null;
    public int lengthOfLongestSubstring(String s) {
        for(int i=0; i<s.length(); i++){
            substr = "" + s.charAt(i);
            for(int j=i+1; j<s.length()-i-1; j++){
                if(!substr.contains(s.charAt(j))){
                    substr = substr + "" + s.charAt(j);
                } else {
                    longestStr = longestStr.length > substr.length? longestStr:substr;
                }
        }
    }
    return longestStr.length;
}
}
// @lc code=end

