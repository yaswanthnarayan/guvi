st=input()
lp=[]
sbst=""
if st==st[::-1]:
    lp.append(0)
else:
    for i in range(0,len(st)-1):
        for j in range(i+1,len(st)):
            sbst=st[i:j+1]
            if sbst==sbst[::-1]:
                lp.append(len(st)-len(sbst))
print(min(lp))
