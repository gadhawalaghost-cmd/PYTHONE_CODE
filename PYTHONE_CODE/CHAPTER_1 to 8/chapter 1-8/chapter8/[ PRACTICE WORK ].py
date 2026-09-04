# Create a student class that take name & marks of 3 subjects as arguments in constructor.
# then create a method to print the average.

class student :
    
    def __init__(self,name,marks) :
        self.name = name
        self.marks = marks

    def get_avg (self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is", sum/3 )
        
s1 = student("karan",[87,98,67])
print(s1.name,s1.marks)
s1.get_avg()




# Create account class with 2 attributes- balance & account no.
# Create meathod for debit,creadit & printing the balance.

class Account:


    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no

    # debit method
    def debit(self,amount):
        self.balance =- amount
        print("Rs.", amount,"was debited")
        print("total balance =", self.get_balance())


    # creadit method
    def creadit(self,amount):
        self.balance =+ amount
        print("Rs.", amount,"was debited")
        print("total balance =", self.get_balance())
        
    def get_balance(self):
        return self.balance
   
acc1 = Account(10000, 5678)
acc1.debit(1000)
acc1.creadit(5000)





# Q-1]

class circle :

    def __init__(self,R):
        self.R = R

    def area(self):
        return (22/7) * self.R **2

    def perimiter(self):
        return 2 * (22/7) * self.R


c1 = circle(21)
print(c1.area())
print(c1.perimiter())





# Q-2]

class Employee :
    def __init__(self,role,dep,sal):
        self.role = role
        self.dep = dep
        self.sal = sal

    def details(self):
        return


class Engineer(Employee):

    def __init__(self,name,age):
        self.name = name
        self.age = age

e1 = Employee("HR","cybersecurity",50,000)
e2 = Engineer("raza",18)

print("my job role is:",e1.role)
print("my depatment is:",e1.dep)
print("my salary is:",e1.sal)
print("my name is:",e2.name)
print("my age is:",e2.age)





# Q-3]

class order:

    def __init__(self,item,price):
        self.item = item
        self.price = price


    def __gt__(self,odr2):
        return self.price > odr2.price # thay show true


odr1 = order("milk",700)
odr2 = order("cake",500)
print(odr1 > odr2)
