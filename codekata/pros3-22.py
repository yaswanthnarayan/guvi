n=input()
l=[int(x) for x in input().split()]
ll=[]
for i in range(len(l)):
    x=l[i]
    for j in range(i+2,len(l),2):
        x+=l[j]
        ll.append(x)
print(max(ll))
        
        
