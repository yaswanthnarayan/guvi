n,x,y=map(int,input().split())
if(x+y)==n:
    print("YES")
elif n%(x+y)==0:
    print("YES")
else:
    print("NO")
