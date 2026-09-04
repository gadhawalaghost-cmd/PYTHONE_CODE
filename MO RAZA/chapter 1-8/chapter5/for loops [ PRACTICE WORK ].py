#print the elements of the following list using a loop.
#[1,4,9,16,25,36,49,64,81,100]

num=[1,4,9,16,25,36,49,64,81,100]
for i in num:
    print(i)




#search for a number X in this tuple using loop:
#(1,4,9,16,25,36,49,64,81,100)

num=(1,4,9,16,25,36,49,64,81,100)
x=81

idx = 0
for el in num:
    if(el == x):
        print("number found at index:",idx)
    idx +=1
print("stop")




#print number from 1 to 100,using range().

for i in range(1,101):
    print (i)



    
#print number from 100 to 1,using rang().

for i in range(100,0,-1):
    print(i)
    



#print the multiplication table of a number n,using range()

n=int(input("enter number:",))
for i in range(1,11):
    print(n*i)




#wap to find the factorial of find numbers.


n=4
fact=1

for i in range(1,n+1):
    fact *= i
print("factorial=",fact)