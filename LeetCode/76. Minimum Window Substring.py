# Solution 1: Sliding window using dict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        left = right = -1
        
        t_char_bag = dict()
        
        # create initial char bag
        for char in t:
            if char in t_char_bag:
                t_char_bag[char] += 1
            else:
                t_char_bag[char] = 1

        # find first matching char in s & t
        for i in range(len(s)):
            if s[i] in t_char_bag:
                left = i
                right = i
                t_char_bag[s[i]] -= 1
                break

        if max(t_char_bag.values()) == 0:
            return ''.join(s[left:right+1])

        # no matching char between s & t
        if left == -1:
            return ""

        # find first right index where s[left:right] contains all of t chars
        while max(t_char_bag.values()) > 0 and right < len(s)-1:
            right += 1

            if s[right] in t_char_bag:
                t_char_bag[s[right]] -= 1

        # no such right index found
        if max(t_char_bag.values()) > 0:
            return ""

        # calculate first window length and first string
        max_window_len = right - left + 1
        res = s[left:right+1]


        # squeeze first window from left
        while max(t_char_bag.values()) == 0 and (s[left] not in t_char_bag or t_char_bag[s[left]] < 0):
            if t_char_bag.get(s[left], 1) < 0:
                t_char_bag[s[left]] += 1
            left += 1

            if max_window_len > right - left + 1:
                max_window_len = right - left + 1
                res = s[left:right+1]


        
        # keep moving the entire window until you find another position where s[left:right] contains all of t
        while right != len(s) - 1:
            if s[left] in t_char_bag:
                t_char_bag[s[left]] += 1
            left += 1
            
            right += 1
            if s[right] in t_char_bag:
                t_char_bag[s[right]] -= 1
            
            # if you find another valid window, start squeezing window from left to find min
            while max(t_char_bag.values()) == 0 and (s[left] not in t_char_bag or t_char_bag[s[left]] < 0):
                if t_char_bag.get(s[left], 1) < 0:
                    t_char_bag[s[left]] += 1
                left += 1
            
            # check if new window size < prev window
            if max_window_len > right - left + 1:
                max_window_len = right - left + 1
                res = s[left:right+1]
        
        # the last window is the one where right of the window is last element of list, squeeze from left one last time
        while max(t_char_bag.values()) == 0 and (s[left] not in t_char_bag or t_char_bag[s[left]] < 0):
            if t_char_bag.get(s[left], 1) < 0:
                t_char_bag[s[left]] += 1
            left += 1
            
            if max_window_len > right - left + 1:
                max_window_len = right - left + 1
                res = s[left:right+1]
        
        return ''.join(res)


# Solution 2: Same approach, more concise code

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)  # elements required
        window = dict()  # elements in current window

        chars_matched = 0
        chars_reqd = len(required.keys())  # number of distinct chars required to be matched

        l = r = 0
        final_l = final_r = 0
        min_len = len(s)

        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1  # add current right element to window

            if s[r] in required:
                if window[s[r]] == required[s[r]]:
                    chars_matched += 1

                while chars_matched == chars_reqd:
                    # compress from left while reqd matches window chars
                    if r-l+1 <= min_len:
                        min_len = r-l+1
                        final_l = l
                        final_r = r+1

                    if s[l] in required and window[s[l]] == required[s[l]]:
                        chars_matched -= 1

                    window[s[l]] -= 1
                    l += 1

            r += 1

        return s[final_l:final_r]