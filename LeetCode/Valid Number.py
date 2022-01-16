class Solution:
    def isDecimal(self, i):
        if i in ['inf', '-inf', '+inf', 'infinity', '-infinity', '+infinity']:
            return False
        try:
            float(i)
            return True
        except ValueError:
            return False

    def isInteger(self, i):
        if i in ['inf', '-inf', '+inf', 'infinity', '-infinity', '+infinity']:
            return False
        try:
            int(i)
            return True
        except ValueError:
            return False

    def isNumber(self, s: str) -> bool:
        s = s.lower()
        s = s.split('e')
        
        if len(s) > 2:
            return False
        
        if len(s) == 1:
            return self.isDecimal(s[0]) or self.isInteger(s[0])
        
        if len(s) == 2:
            first = self.isDecimal(s[0]) or self.isInteger(s[0])
            second = self.isInteger(s[1])

            return first and second