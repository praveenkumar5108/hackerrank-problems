def solution(N):
    count = 0
    n = 2
    while 2*N+n-n**2 > 0:
        a = (2*N+n-n**2)/(2*n)
        if a - int(a) == 0:
            print(a,n)
            count += 1
        n += 1
    return count
print(solution(10))
