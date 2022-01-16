# 1048. Longest String Chain

# 1st Approach
# [working but TLE ~1800ms on worst case]
class Solution:
    def predecessor(self, p, s):
        for i in range(len(s)):
            if s[:i] + s[i+1:] == p:
                return True
        return False
    
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        len_words = len(words)
        word_chain_map = list()
        
        len_list = [len(w) for w in words]
        
        for i in range(len_words):
            word_chain_map.append(1)
            for j in range(i-1, -1, -1):
                if len_list[i] - len_list[j] > 1:
                    break
                if self.predecessor(words[j], words[i]):
                    word_chain_map[i] = max(word_chain_map[i], word_chain_map[j] + 1)
        
        return max(word_chain_map)

# 2nd Approach - Optimising 1st approach using dict instead of list
# [working and ~150ms on worst case]
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(set(words), key=len)
        max_chain_len = 1

        word_chain_map = dict()

        for i in range(len(words)):
            curr_max_chain = 1
            current_word = words[i]

            for j in range(len(current_word)):
                if current_word[:j] + current_word[j+1:] in words[:i]:
                    curr_max_chain = max(curr_max_chain, word_chain_map[current_word[:j] + current_word[j+1:]] + 1)

            word_chain_map[current_word] = curr_max_chain
            max_chain_len = max(max_chain_len, curr_max_chain)

        return(max_chain_len)