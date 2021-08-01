#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        longeststr = ""
        for i in range(len(s)):
            substr = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in substr:
                    substr += s[j]
                elif s[j] in substr:
                    longeststr = substr if len(substr) > len(longeststr) else longeststr
                    break
                longeststr = substr if len(substr) > len(longeststr) else longeststr

            if len(s) == 1:
                longeststr = s
        return len(longeststr)

if __name__ == "__main__":
    solution = Solution()
    solution.lengthOfLongestSubstring(s="au")
        
# @lc code=end

