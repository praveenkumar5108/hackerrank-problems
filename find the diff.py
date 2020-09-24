from collections import Counter
def diff(t,s):
    return list((Counter(t)-Counter(s).keys()))[0]
