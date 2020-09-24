class Solution:
    def rom(self,s):
        numerals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        last = 0
        number = 0
        for i in range(len(s)):
            new = numerals[s[i])
            if new > last:
                new += new-2*last
            else:
                number += new
            last new
        return number
