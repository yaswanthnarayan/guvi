dummy = int(input())
s=[]
n = [int(x) for x in input().split()]
n.sort(reverse=True)
for i in range(0,dummy):
    if(i%2==0):
        s.append(max(n))
        n.remove(max(n))
    else:
        s.append(min(n))
        n.remove(min(n))
for i in range(len(s)):
    if(i<=len(s)-2):
        print(s[i],end=" ")
    else:
        print(s[i],end="")
