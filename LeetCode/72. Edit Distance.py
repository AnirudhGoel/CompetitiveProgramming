# 72. Edit Distance

# Solution 1: 94.60% Faster
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def calcDistance(mem, word1, word2, i1, i2):
            if i1 == len(word1):
                return len(word2) - i2
            
            if i2 == len(word2):
                return len(word1) - i1
            
            if mem[i1][i2]:
                return mem[i1][i2]
            
            if word1[i1] == word2[i2]:
                mem[i1][i2] = calcDistance(mem, word1, word2, i1 + 1, i2 + 1)
                return mem[i1][i2]
            
            inse = calcDistance(mem, word1, word2, i1, i2 + 1)
            dele = calcDistance(mem, word1, word2, i1 + 1, i2)
            chan = calcDistance(mem, word1, word2, i1 + 1, i2 + 1)
            
            mem[i1][i2] = min(inse, dele, chan) + 1
            
            return mem[i1][i2]
        
        if not word1:
            return len(word2)
        
        if not word2:
            return len(word1)
        
        mem = [[None for _ in range(len(word2))] for _ in range(len(word1))]
        
        return calcDistance(mem, word1, word2, 0, 0)