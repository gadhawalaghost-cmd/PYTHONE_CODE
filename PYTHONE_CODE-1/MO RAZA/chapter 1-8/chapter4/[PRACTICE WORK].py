# store following word meanings in a pythone dictionary.

dic={
    "table":["a pice of furniture","list of facts & figuare"],
    "cate": "a small animel"
}
print (dic)

# you are given a list of subject for students.
#  assume one classroom is recuired for 1 subject.
# how many classrroms are needed by all students.

classrrom={
    "python","java","c++","python","javascript","java",
     "python","java","c++","c"
           }
print(len(classrrom))

# wap to enter marks of 3 subjects from the user and store them in a dictionary.
# start with an empty dictionary & add one by one. use subject name as key & marks as value

marks={ }
phy=int(input("put phy marks :"))
marks.update({"phy":phy})


chem=int(input("put chem marks :"))
marks.update({"chem":chem})

math=int(input("put math marks :"))
marks.update({"math":math})

print(marks)

# figure out a way to store 9 & 9.0 as seperate values in the set.
# (you can take help of bilt-in data types)

set={
    ("float",9.0),
    ("int",9)
}
print (set)