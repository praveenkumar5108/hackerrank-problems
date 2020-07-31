class Solution:
    def lastofWord(str() s):
        count = 0
        n = s.size()
        i = 0
        while(i<n):
            if(s[i] != ' '):
                count += 1
                i += 1
            else:
                while(i<n and sS[i]== ' '):
                    i += 1
                    if(i==n):
                        return count
                    else:
                        count = 0
        return count

lastWord('Praveen Kumar')
