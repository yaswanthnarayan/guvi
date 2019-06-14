data=[int(x) for x in input().split(" ")]
sol=0
tl=[int(x) for x in input().split(" ")]
share=int(input())
total=sum(tl)
tcost=(total-tl[data[1]])//2
if (tcost==share):
    print("Bon Appetit")
else:
    print(int(tl[data[1]]/2))

