# # CODE 1 / 750: (BASIC)
# # user se 2 numbers lo aur unka sum,subs,multi,division print karo.

# num1 = int(input("enter 1st number:"))
# num2 = int(input("enter 2nd number:"))

# print (num1 + num2)
# print (num1 - num2)
# print (num1 * num2)
# print (num1 / num2)





# #  CODE 2 / 750: (CONDITIONS)
# #  user se ek number lo aur check karo ki number positive,negetiv aur zero hai?

# num1 = int(input("enter your number:"))

# if num1 == 0 :
#     print("your number is zero")

# if num1 <= 0 :
#     print("your number is nagative")

# if num1 >= 0:
#     print("your number is posative")




# #  CODE 3 / 750: (LOOPS)
# # 1 se 50 tak ke sare even number print karo.

# i = 1

# while i <= 50:
#     i += 1
# print (i)





# #  CODE 4 / 750:(STRING)
# # user se ek string lo aur count karo ki usme vowels (a,e,i,o,u) kitne hai

# vo = "aeiou"
# str1 = input("enter your string:")
# count = 0
# for i in str1 :
#     if str1.count(vo):
#         count += 1
# print(count) 





# # CODE 5 / 750:(LOGIC + LOOP)
# # user se ek number N lo aur 1 se N tum ke number ka sum calculte karo.


# n = int(input("enter your number:"))
# sum = 0
# i = 1

# while i <= n :
#     sum += i
#     i += 1
# print(sum)





# CODE 6 / 750:(list)
# user se 5 number ki list lo aur sabse bada number find karo.

# l1 =eval(input("enter five number of list:"))
# larg = max(l1)
# print("larges number is:",larg)





# CODE 7 / 750: (ODD & EVEN)
# ek list main numbers lo aur cont karo ki usme kitne even aur kitne odd numbers hain.

# l1 = [2,4,1,6,8,4,9,14,11,0]
# odd = 0
# even = 0

# for number in l1:
#     if number %2 == 0:
#           even += 1
#     else :
#          odd += 1

# print("even numbers:",even)
# print("odd numbers:",odd)





# CODE 8 / 750: (STRING REVERSE)
# user se ek string lo aur usko reverse kerke print karo.

# s1 = input("enter your list:")
# revers = s1 [:: -1]
# print("reverse:",revers)





# CODE 9 / 750: (PRIME NUMBER CHEACK)
# USER SE EK NUMBER LO AUR CHECK KARO KI WOH PRIME NUMBER HAI YA NAHI.

# num1 = int(input("enter one number:"))

# count = 0

# for i in range(1,num1 +1):
#     if num1 %i == 0:
#         count += 1

# if count == 2 :
#         print("prime number")
# else:
#         print("not a prime number")




# CODE 10 / 750: (CREATE CALCULATUR)
# ek function calculator() banao jo:
# additoion +
# subtraction -
# multiplication *
# division /        PERFORM KARO.

# def calculator (a,b,operator):

#     if operator == "+" :
#         print (a + b)

#     if operator == "-" :
#         print (a - b)

#     if operator == "*" :
#         print (a * b)

#     elif operator == "/" :
#         print (a / b)

#     else:
#         print("invalin operation")

# a = int(input("enter your first number:"))
# oprator = input("enter your operator:")
# b = int(input("enter your second number:"))

# calculator(a, b, oprator).