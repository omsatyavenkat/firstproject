n=int(input("enter n value:"))
f1,f2,f3=0,1,0
for i in range(1,n+1):
    f3=f1+f2
    print(f1,end=" ")
    f1=f2
    f2=f3
