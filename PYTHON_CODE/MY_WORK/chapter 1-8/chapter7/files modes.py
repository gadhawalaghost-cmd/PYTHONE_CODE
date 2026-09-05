
#"R" : used for read data/file

f = open(r"C:\MO RAZA\practice code.py\raza.txt","r")

data = f.read()
print(data)

f.close()




# "w" : used for write data/file, with trunkating the file first.

f = open(r"C:\MO RAZA\practice code.py\raza2.txt","w")

data = f.write("i am learning file i/o,in python")
print(data)

f.close()




# "a" : used for append data/file at the end.

f = open(r"C:\MO RAZA\practice code.py\raza2.txt","a")

f.write("\n i am learning file i/o,in java")

f.close()