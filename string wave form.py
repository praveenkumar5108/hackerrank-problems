def waveForm(arr,n):
    arr.sort();
    for i in range(0,n-1,2):
        arr[i],arr[i+1] = arr[i+1],arr[i]

arr = [10,80,332,55,2,3,45]
waveForm(arr,len(arr))
for i in range(0,len(arr)):
    print(arr[i]);
