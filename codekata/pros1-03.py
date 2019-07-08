x,y=input().split()
def check(x,y):
    count=0
    for i in range(len(x)):
            if x[i]!=y[i]:
                count+=1
            if i==(len(x)-1):
                count+=abs(len(x)-len(y))
    return count
if x==y:
    print(0)
elif len(x)<=len(y):
    print(check(x,y))
else:
    print(check(y,x))
