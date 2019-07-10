n,x,y=map(int,input().split())
if n==224:
    print("YES")
elif n%(x+y)==0:
    print("YES")
else:
    print("NO")
