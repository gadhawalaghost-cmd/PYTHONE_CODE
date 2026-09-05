# __init__ function:
# All class have a function called __init__(),
# witch is always is exicuted when the object is being initiated.

class student:

    def __init__ (self,name,marks):  # This function are call it self automaticlly.
        self.name = name
        self.marks = marks

s1 = student("karan",94)
print(s1.name,s1.marks)

s2 = student("rahul",67)
print(s2.name, s2.marks)

print("adding new student and marks")