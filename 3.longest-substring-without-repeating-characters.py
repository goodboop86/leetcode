#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dic = {}
        longest_size = 0
        position = 0

        for i, ch in enumerate(s):
            if ch in char_dic:
                # charが当たるたびに距離を更新
                longest_size = max(longest_size, i-position)
                # 前回のchar時点までpositionを更新する
                position = max(position, char_dic[ch]+1)
            char_dic[ch]=i
        # 最終idx時にはpositionが更新できていない可能性がある
        return max(longest_size, len(s)-position)

if __name__ == "__main__":
    solution = Solution()
    solution.lengthOfLongestSubstring(s="abcabcbb")
        
# @lc code=end

