# Create a file "practice.txt" using pythone. add the following data.
# Hi everyone.
# we are learning i/o.
# using java.
# i like programing in java.

# with open("C:\MO RAZA\practice code.py\practice.txt","w")as f:
#     f.write ("Hi everyone\nwe are learning i/o\nusing ava\ni like programing in java" )
    



# Waf that replace all occurunces
# of "java" with "pythone" in above file

# with open("C:\MO RAZA\practice code.py\practice.txt","r")as f:
#     data = f.read()

# new_data = data.replace("java","pythone")
# print(new_data)

# with open("C:\MO RAZA\practice code.py\practice.txt","w")as f:
#     f.write(new_data)




# search if the world "learning" 
# exists in the file or not

# with open("C:\MO RAZA\practice code.py\practice.txt","r")as f :
#     data = f.read()
#     if (data.find("learning") != -1):
#         print("exist in the file")
#     else :
#         print("not exist in the file")




# WAF to find in witch line of the file does the word,
#  "learning",occur first.
# print -1 if word not found.


# def cheak_line():
#  word= "learning"
#  data = True
#  line_no = 1
#  with open (r"C:\MO RAZA\practice code.py\raza.txt","r")as f:
#     while data:
#       data = f.readline()
#       if word in data :
#         print (line_no)
#       line_no += 1


#  return -1
# cheak_line()




# From a file contain number saprated by comma,
# print the count of even number.

count = 0
with open (r"C:\MO RAZA\practice code.py\raza2.txt","r")as f:
    data = f.read ()

    num = data.split(",")
    for val in num:
        if (int(val) %2==0):
            count += 1

print (count)