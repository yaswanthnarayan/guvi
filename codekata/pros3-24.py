from itertools import permutations,combinations_with_replacement
n=int(input())
ll=[]
sl=[]
com=combinations_with_replacement(['0','1'], n)
for i in list(com):
    p=permutations(list(i))
    for i in list(p):
        x=("".join(i))
        if x not in ll:
            ll.append(x)
            print(x)

