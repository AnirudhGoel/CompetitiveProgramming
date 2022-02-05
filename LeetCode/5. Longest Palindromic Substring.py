# 5. Longest Palindromic Substring
# My approach is almost as good (probably even better) as the Approach 4 of the solution. They expand around every letter and make function calls for every letter. I filter out possible centers first and then expand around only those. Glad that I came up with this myself. :)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = list()
        len_s = len(s)
        max_palin_len = 1
        
        try:
            for i in range(len_s):
                if s[i] == s[i+1]:
                    palindromes.append([i, i+1])
                
                if s[i] == s[i+2]:
                    palindromes.append([i, i+2])
        except IndexError:
            pass
        
        if not palindromes:
            return(s[0])
        
        for palin in palindromes:
            l = palin[0]
            r = palin[1]
            
            while l > 0 and r < len_s - 1:
                if s[l-1] != s[r+1]:
                    break
                l -= 1
                r += 1
            
            palin_len = r - l + 1
            if palin_len > max_palin_len:
                max_palin_len = palin_len
                max_palin = s[l:r+1]
        
        return(max_palin)