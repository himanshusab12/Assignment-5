row = int(input("Enter number of rows"))
y=0
asc = 65
for x in range(1,row+1):
    while y<x:
        print(chr(asc),end="")
        y+=1
        asc+=1
    y=0
    print()
