# 22. Generate Parentheses

# Iterative DFS solution
class Solution:
    def isWellFormed(self, n, word):
        num_open_brac = 0
        stack = list()
        
        for w in word:
            if w == '(' and num_open_brac < n:
                num_open_brac += 1
                stack.append(w)
            elif w == ')' and stack:
                stack.pop()
            else:
                return False
        return True
    
    def generateParenthesis(self, n: int) -> List[str]:
        store = ['(']  # n >= 1
        
        while len(store[0]) < n*2:
            curr = store.pop(0)
            
            if self.isWellFormed(n, curr + '('):
                store.append(curr + '(')
            
            if self.isWellFormed(n, curr + ')'):
                store.append(curr + ')')
        
        return store

# Recursive + Backtracking Solution (97.58% faster)
class Solution:
    def generateP(self, n, open, close, curr, store):
        if len(curr) == n*2:
            store.append(curr)
            return

        if open < n:
            self.generateP(n, open+1, close, curr+'(', store)

        if close < open:
            self.generateP(n, open, close+1, curr+')', store)

    def generateParenthesis(self, n: int) -> List[str]:
        open = 1
        close = 0
        store = []
        curr = '('

        self.generateP(n, open, close, curr, store)

        return(store)