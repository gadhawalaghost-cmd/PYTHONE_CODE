# when you create one student class,
# and this class have student by different name of object. it's call instance.
# and this all object have same class name, it call class attribute.

class student:
    class_no = 123 # class attributes, it will define for all obects you create.

    def __init__(self,name,) : # instance attributes, have each different objects.
        self.name = name    # call it self.

s1 = student("ayan")
print(s1.name,s1.class_no)

s2 = student("farhan")
print(s1.name,s1.class_no)