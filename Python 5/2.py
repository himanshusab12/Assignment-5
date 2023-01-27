start = int(input("Enter the starting point of the range"))
en = int(input("Enter the ending point of the range"))
val = int(input("Enter the value to check divisbility"))
for a in range(start,en+1):
    if a%val==0:
        print(a,end=" ")

