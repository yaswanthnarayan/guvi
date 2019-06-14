st=input()
li=[]
for i in range(0,len(st)):
    if st[i] in li:
            break
    else:
        li.append(st[i])
print(len(li))
