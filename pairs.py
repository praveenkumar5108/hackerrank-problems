from collections import Counter
n,k = map(int,input().split())
arr = list(map(int,input().split()))
counter = Counter(arr)
count = 0
for i in arr:
    find = i-k
    if(find in counter):
        count += 1
print(count)
