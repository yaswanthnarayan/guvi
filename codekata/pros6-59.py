x,y=input().split("|")
z=input()
if(len(x)==len(y)):
    print("Impossible")
elif(len(x)!=len(z+y)):
    print("Impossible")
elif(len(x)==len(z+y)):
    print(x+"|"+y+z)
