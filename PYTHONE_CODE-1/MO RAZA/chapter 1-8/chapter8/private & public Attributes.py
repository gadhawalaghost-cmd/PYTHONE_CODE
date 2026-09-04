
# Print Attributes & methods are mean to be used only within the class and are not,
# Accessible from outside the class

# class Account :
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass #put 2 underscode (_ _)at starting object/method to keep priveta.

# acc1 = Account("2468","xyz")
# print(acc1.acc_no)
# print(acc1.__acc_pass) # now thay giv error # 





# SUPER() METHOD _AND_ @STATICMETHOD
# SUPER() METHODS is used to access methods of the parent class.
# @STATICMETHOD are a function that not need any object and class
# class car:
#     def __init__(self,type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car starting..")

#     @staticmethod
#     def stop():
#         print("car are stoped")

# class toyotacar(car):
#     def __init__(self,name,type):
#         self.name = name
#         super().__init__(type)
#         super().stop()

# car1 = toyotacar("prius","CNG")
# print(car1.name)
# print(car1.type)
# car1.start()




# @CLASSMEHOD:
# @CLASSMETHOD used for take hole data of class.
# thay work only for class not object.

class student:
    school_name = "246 xyz"

    @classmethod
    def s_name (cls): # put (cls) to run classmethod
        print(cls.school_name)

student.s_name()
