# Top-Down Dynamic Programming (Recursion + Memoization)

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)
        mem = dict()
        ans = 0
        
        for word in words:
            ans = max(ans, self.dfs(words, mem, word))
            
        return ans
                
#     def calculateMaxStr(self, words, mem, word, level):
#         for i in range(len(word)):
#             sub_word = word[:i] + word[i+1:]
#             level = 0
#             if sub_word in words:
#                 if len(sub_word) == 1:
#                     mem[sub_word] = 1
#                     return 1
                
#                 level = max(level, 1 + self.calculateMaxStr(words, mem, sub_word))
#                 mem[sub_word] = level
#             else:
#                 mem[sub_word] = level
                
    def dfs(self, words, mem, word):
        if word in mem:
            return mem[word]
        
        max_length = 1
        
        for i in range(len(word)):
            sub_word = word[:i] + word[i+1:]
            
            if sub_word in words:
                current_length = 1 + self.dfs(words, mem, sub_word)
                # current_length is, iss sub_word k lie jo length aayi h poora traverse krke
                max_length = max(max_length, current_length)
                # max_length is, iss level pr jitne sub_words h yaa is 'word' k lie jitne 'sub_word'(s) abhi tk traverse kr lie h, unme se max length
                
        mem[word] = max_length
        
        return max_length