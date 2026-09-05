#Print number from 1 to 100.

i = 1
while i <= 100 :
    print (i)
    i += 1
print("end of the number count")




#print number from 100 to 1.

i = 100
while i >= 1 :
   print (i)
   i -=1
print("end of the number count")





#print the multiplication tabel of a number n.

i =1
while i<=10 :
    print(6*i)
    i +=1




#print the elements of the followink list using loop:
#[1,4,9,16,25,36,49,64,81,100]

x=[1,4,9,16,25,36,49,64,81,100]
i=0
while i < len(x):
    print(x[i])
    i += 1




#search for a number X in this tuple using loop:
#(1,4,9,16,25,36,49,64,81,100)

num=(1,4,9,16,25,36,49,64,81,100)

x=64

i=0
while i < len(num):
    if(num [i] == x):
        print("found at index",i)
    i +=1




#wap to find the sum of first n numbers.

n=5
sum=0
i=1
while i <= n:
    sum += i
    i += 1
print("total sum=",sum)
