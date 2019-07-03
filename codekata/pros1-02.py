from itertools import combinations
a,b = [int(x) for x in input().split()]
n = str(a)
s = list(combinations(n,len(n)-b))
s.sort()
print("".join(s[0]))
