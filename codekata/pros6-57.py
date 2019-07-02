x,y=input().split()
l=[]
r=[]
for i in range(len(x)):
    a=x[i:i+2]
    if(len(a)==2):
        l.append(a)
for i in range(len(y)):
        b=y[i:i+2]
        if(len(b)==2):
            r.append(b)
for i in l:
    if i in r:
        c=1
        break
    else:
        c=-1
if c==1:
    print("yes")
else:
    print("no")
