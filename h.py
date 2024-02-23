n=int(input("enter the weight"))
if n>2 and n%2==0:
    for i in range(2,n//2+1,2):
        print("[",i,",",n-i,"]",end = " " )
else:
    print("no")