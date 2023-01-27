import math
s1 = int(input("Enter first side of triangle"))
s2 = int(input("Enter second side of triangle"))
s3 = int(input("Enter third side of triangle"))
if (s1+s2)>s3 or (s1+s3)>s2 or (s2+s3)>s1:
    s = (s1+s2+s3)/2
    area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    print(area)
else:
    print("Wrong Input")
