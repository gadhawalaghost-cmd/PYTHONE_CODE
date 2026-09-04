a= int(input("first number:"))
b= int(input("second number:"))
c= int(input("third number:" ))
d= int(input("fourth number:" ))

if (a >= b and a >=c and a>=d):
    print("first number is greatest:")

elif (b >=c and b>=d):
    print("second number is greatest:")

elif (c >=d):
    print("third number is greatest:")

else:
    print("fourth number is greatest:")