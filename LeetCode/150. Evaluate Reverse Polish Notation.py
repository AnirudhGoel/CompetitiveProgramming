# 150. Evaluate Reverse Polish Notation

# Solution 1: Dirty solution using eval - slow and not interview level
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        
        for i in tokens:
            try:
                i = int(i)
                stack.append(i)
            except ValueError:
                n1 = stack.pop()
                n2 = stack.pop()
                
                stack.append(int(eval(f'{n2} {i} {n1}')))
        return stack.pop()

# Solution 2: 65% faster and much better
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()

        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 / n1))
            else:
                stack.append(int(i))
        return stack.pop()