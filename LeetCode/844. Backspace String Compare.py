# 844. Backspace String Compare

# Sol 1: Time: O(n), Space: O(s+t)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = ''
        s2 = ''
        
        for i in s:
            if i == '#':
                s1 = s1[:-1]
                continue
            s1 += i
        
        for j in t:
            if j == '#':
                s2 = s2[:-1]
                continue
            s2 += j
        
        return (s1 == s2)


# Sol 2: Time: O(n), Space: O(1)