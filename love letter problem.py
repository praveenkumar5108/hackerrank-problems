s = input()
print (sum(map(lambda x: abs(ord(s[x]) - ord(s[len(s) - x - 1])), range(len(s)/2))))
