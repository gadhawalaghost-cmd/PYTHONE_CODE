# CODE 1 / 750: (BASIC)
# user se 2 numbers lo aur unka sum,subs,multi,division print karo.

# num1 = int(input("enter 1st number:"))
# num2 = int(input("enter 2nd number:"))

# print (num1 + num2)
# print (num1 - num2)
# print (num1 * num2)
# print (num1 / num2)





#  CODE 2 / 750: (CONDITIONS)
#  user se ek number lo aur check karo ki number positive,negetiv aur zero hai?

# num1 = int(input("enter your number:"))

# if num1 == 0 :
#     print("your number is zero")

# if num1 <= 0 :
#     print("your number is nagative")

# if num1 >= 0:
#     print("your number is posative")




#  CODE 3 / 750: (LOOPS)
# 1 se 50 tak ke sare even number print karo.

# i = 1

# while i <= 50:
#     i += 1
# print (i)





#  CODE 4 / 750:(STRING)
# user se ek string lo aur count karo ki usme vowels (a,e,i,o,u) kitne hai

# vo = "aeiou"
# str1 = input("enter your string:")
# count = 0
# for i in str1 :
#     if str1.count(vo):
#         count += 1
# print(count) 





# CODE 5 / 750:(LOGIC + LOOP)
# user se ek number N lo aur 1 se N tum ke number ka sum calculte karo.


n = int(input("enter your number:"))
sum = 0
i = 1

while i <= n :
    sum += i
    i += 1
print(sum)