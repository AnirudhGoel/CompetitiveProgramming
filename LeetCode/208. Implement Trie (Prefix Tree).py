# 208. Implement Trie (Prefix Tree)

# Solution 1: Can be improved by creating a TrieNode object
class Trie:

    def __init__(self):
        self.nextChars = dict()

    def insert(self, word: str) -> None:
        curr = self.nextChars
        
        for i in range(len(word)):
            if word[i] in curr:
                curr = curr[word[i]]
                if i == len(word) - 1 and curr['end'] is False:
                    curr['end'] = True
            
            else:
                curr[word[i]] = dict()
                curr[word[i]]['end'] = False
                if i == len(word) - 1:
                    curr[word[i]]['end'] = True
                
                curr = curr[word[i]]

    def search(self, word: str) -> bool:
        curr = self.nextChars
        
        for i in range(len(word)):
            if word[i] in curr:
                curr = curr[word[i]]
                
                if i == len(word) - 1:
                    return curr['end']
            else:
                return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.nextChars
        
        for i in range(len(prefix)):
            if prefix[i] in curr:
                curr = curr[prefix[i]]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)