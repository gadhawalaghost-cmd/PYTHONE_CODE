# WAF to print the length of a list.(list in the parameter)

list1 = [2,4,6,8,10]
list2= [1,3,5,7,9]
  
def print_len (list):
    print (len(list))

print_len(list1)

print_len(list2) 




# WAF TO print the element of a list in a singl

list = [2,4,6,8,10]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list (list)




# WAF to find the factorial of n.

n = 5

def cal_fact(n):
    fact = 1
    for i in range (1,n+1):
        fact *= i
    print (fact)

cal_fact(5)




# WAF to convert usd in to inr.

def converter(usd_val):
    inr_val = usd_val *97
    print(usd_val,"USD =", inr_val, "INR")

converter(10) 



# :H/W LESSION : input one number,
#  when it's odd print string odd or print string even (using function).

a = int(input("enter one number:",))

def odd_even (a):
    if a %2== 0 :
        print("EVEN")
    else:
        print("ODD")

odd_even(a)




# RECURSION
#  war funtion to calculate the sum of first n natural number.

def sum(n):
    if (n == 0):
     return 0
    return sum(n-1)+n

cal =sum(5)
print(cal)