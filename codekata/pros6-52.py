l=[]
n=[]
for i in range(4):
    l.append(input().split())
for i in range(len(l)):
    a=l[i]
    x=abs(int(a[0])-int(a[1]))
    n.append(x)
if(n[0]==n[2]) and (n[1]==n[3]):
    print("yes")
else:
    print("no")
        
    
