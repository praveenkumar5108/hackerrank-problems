num = int(input())
Reverse = 0
while(num>0):
    rem = num%10
    Reverse = (Reverse*10)+rem
    num = num//10
print(Reverse)
