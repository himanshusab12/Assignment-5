n = int(input("Enter the range of pattern"))
x =1
check = 0
for a in range(0,n):
    for y in range(0,x):
        print('*',end=" ")
    if(x==n-int(n/2) or check==1):
        x-=1
        check = 1
    else:
        x+=1
    print()
