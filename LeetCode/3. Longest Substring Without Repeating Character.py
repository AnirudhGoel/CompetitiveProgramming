# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = dict()
        l = 0
        r = 0
        max_length = 0
        len_s = len(s)
        
        if len_s <= 1:
            return(len_s)
        
        for i in range(len_s):
            if s[i] not in char_map or char_map.get(s[i], len_s + 1) < l:
                r = i
            else:
                l = char_map[s[i]] + 1
                r = i
            
            char_map[s[i]] = i
            max_length = max(max_length, r-l+1)
        
        return(max_length)