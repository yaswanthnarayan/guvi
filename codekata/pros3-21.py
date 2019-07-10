n=int(input())
l=list(map(int,input().split()))
e=int(n/2)
fh=l[:e]
sh=l[e::]
if ((sum(fh)//len(fh))==(sum(sh)//len(sh))):
    print("yes")
else:
    print("no")
