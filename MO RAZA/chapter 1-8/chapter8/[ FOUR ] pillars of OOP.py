# ABSTRACTION #
# Hiding the implementation details of a class and only showing the essential features to the user.

from builtins import print


class car :
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = car()
car1.start()

# THIS IS CALLED "ABSTRACTION", THAY NEVER SHOW THE STEPS OF CREATING OBJECT





# ENCAPSULATION #
# Wrapping data and function into a single unit (object).

# that mean you dont create a variable,you create function to run code.





# INHARITANCE #
# insaritance have four (4) types of level.

# [1] SINGLE LEVEL INHERITANCE:
# Thay have one parent class and one child class.

class animal:
    def voice(self):
        print("animel have voice")

class dog(animal): # that mean dog are extend from animel class: now thay can access all function from animal class.
     def __init__(self,bark):
        self.bark = bark
        

d1 = dog("dog can bark")
d1.voice()
print(d1.bark)





# [2] MULTILEVEL INHERITANCE:
# Thay have one grand parent,one parent and one child class.

class animal:
    def voice(self):
        print("animel have voice")

class dog(animal): # extend from animel class.
    def color(self):
         print("dog have black color")
        

class dog_cubs(dog): # extend from dog class.
    def __init__(self,cub_color):
        self.cub_color = cub_color

c1 = dog_cubs("cubs have same as dog color")
c1.voice()
c1.color()
print(c1.cub_color)





# [3] HAIRACHICLE INHARITANCE :
# thay have one parent class and two chield class.


class animal:
    def voice(self):
        print("animel have voice")

class dog(animal): # extend from animel class.
    def __init__(self,bark):
      self.bark = bark 

d1 = dog("BARK BARK")
d1.voice()
print (d1.bark)

class cat(animal): # extend from animel class.
    def __init__(self,meow):
        self.meow = meow

c1 = cat("MEOW MEOW")
c1.voice
print(c1.meow)





# [4] MULTIPLE LEVEL INHERITANCE:
# thay have two parent class and one child class.

class Father:
    def dad (self):
        print("FATHER")

class Mother:
    def mom (self):
        print("MOTHER")

class Child(Father,Mother) : # Extend from mother ane father.
    def __init__(self,kid):
        self.kid = kid

k1 = Child("i have mother and father")

k1.dad()
k1.mom()
print(k1.kid)





# POLYMORPHISM :
# When the same operator is allowed to have different meaning according to the context
# polymorphism are giv to sum complex no. by dunder function.
# dunder function have two underscode at start and last.
# EX: A.__operater__(B)


class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def shownum(self):
        print(self.real,"i +",self.img,"j")

    def __add__(num1,num2):
        newreal = num1.real + num2.real
        newimg = num1.img + num2.img
        return complex(newreal,newimg)

    def __sub__(num1,num2):
            newreal = num1.real - num2.real
            newimg = num1.img - num2.img
            return complex(newreal,newimg)
    
num1 = complex(2,4)
num1.shownum()

num2 = complex(4,6)
num2.shownum()

num3 = num1 + num2 
num3.shownum()

num4 = num1 - num2 
num4.shownum()
