class LargestNum(str):
    def __lt__(x,y):
        return x+y > y+x
class Solution:
    def LargetN(self,nums):
        largest_num = ''.join(sorted(map(str,num),Key = LargestNum))
        return 0 if largest_num[0]=='0' else largest_num
        
                              
