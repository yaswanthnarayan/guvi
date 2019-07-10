n=int(input())
sq=1
while(sq<=n and sq*2<=n):
    sq=sq*2
if(sq==n):
    print("0")
else:    
    print(n-sq)
