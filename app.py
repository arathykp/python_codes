

from cmath import pi


def power(numbr,n):
    if n !=0:
        numbr = numbr * power(numbr,n-1)
        return numbr
    else:
        return 1





numbr = int(input("Enter radius : "))
area = pi * power(numbr,2)
print(f"area is {area}")
