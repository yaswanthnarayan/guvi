from itertools import permutations,combinations_with_replacement
n=int(input())
l=[]
ll=[]
for i in range(n):
    l.append('0')
    l.append('1')
com=combinations_with_replacement(l, n)
for i in com:
    ll.append("".join(i))
for i in sorted(list((set(ll)))):
    print(i)

