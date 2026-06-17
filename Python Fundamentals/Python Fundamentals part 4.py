# OOPs(Object Oriented Programming):

# Previously we are writing the code in procedural programing ( when we use functions() in the normal code then it is called the procedural programming).
# In objeect oriented programming we use the classes and objects.


# Objects:
          # Objects are the real world entities. They are based on the practical things.

# Classes:
          # Classes are the blueprint or template, based on that objects are created.

# The Example of objects and classes are:
# 1. Every student in the college have their own data so the data is the class and the students are the objects.
# 2. toyota car company given their blue print for how to make cars like size of tire, colour, engine so these are class and they make multiple cars based on that blueprint so the cars are objects.




class student:


# Attributes/Properties
    age = 19
    college = "VIT Bhopal"
    subject = "C++"
    year = "1st year"

# Behaviour/Member functons/Methods: it is nothing but the normal functions. We write it inside a class That's why it is called Behaviour/Member functons/Methods


stu1 = student()
stu2 = student()
print(stu1.age, stu1.college, stu1.subject, stu1.year)
print(stu2.age, stu2.college, stu2.subject, stu1.year)


# Attributes/Properties: these are we write inside our class for example:  age = 19
                                                                        #  college = "VIT Bhopal"
                                                                        #  subject = "C++" 
                                                                        #  year = "1st year"


#  Behaviour/Member functons/Methods: it is nothing but the normal functions. We write it inside a class That's why it is called Behaviour/Member functons/Methods
# ex:
# def fun(): 
    #   print("Hello world")




# Constructor: __init__Method (Constructor are used for to initilize our object)
             
            #  1. we call it every time when we build an object if we dont call it the python interpreter itself call it so it is inbuild function
            #  2. we can write our own constructor by def __init__(self)
            #     (here the self means current instance of the class.we write it in everytime when we make constructor{in short it is calling the properties of the class.})    
            #  3. constructor calls its object only once at the initilization.
            #  4. In python, we only use single constructor in a class.


class student:
    name = "Krishna"


# here at the paretheses the constructor is called by itself (by python interpreter)
stu1 = student()

print(stu1.name)



#  User defined constructor:

class student:
    def __inti__(self):
        print("Constructor was called ...")


stu1 = student()
stu2 = student()


#  User defined constructor:

class student:
    def __inti__(self, name, cgpa):
        self.name = name    #instance attributes
        self.cgpa = cgpa         
        
    def get_cgpa(self):   #instance methods
        return self.cgpa  

stu1 = student("Sarthak Birari", 8.5)
stu2 = student("Ritika Birari", 9)

print(stu1.name)
print(stu2.cgpa)
print(f"{stu1.name} has {stu1.get_cgpa()}")



# There are two types of constructors:
# 1. Default constructor: def __init__(self)
# 2. Parameterized constructor:  def __inti__(self, name, age)


class student:
    # default constructor
    def __init__(self):
        print("default constructor is being called")

stu1 = student()



class car:
    # Parameterized constructor

    def __init__(self, colour, type):

        self.colour = colour
        self.type = type


cust1 = car("black", "SUV")
cust2= car("navy blue", "Sedan")
print(cust1.colour, cust1.type)
print(cust2.colour, cust2.type)


# Class and Instance attributes/properties:

class student:
#     class attributes/properties
    college_name = "VIT Bhopal"

    def __init__(self, name, subject):
    #  Instance attributes/properties
        self.name = name
        self.subject = subject


student1 = student("Sarthak", "Python")
print(student1.name, student1.subject)

student2 = student()
print(student1.college_name)





# Instance methods:

class laptop:

    storage_type = "SSD"

    def __init__(self, Ram, Storage):
        self.Ram = Ram
        self.Storage = Storage 

    def get_info(self):  #instance method
        print(f"The laptop has {self.Ram} & {self.Storage} {self.storage_type}")

laptop1 = laptop("16gb", "512gb")
laptop2 = laptop("8gb", "256gb")

laptop1.get_info()

# Things to remember: 1. The 1st parameter in the instance method is self
#                     2. Both the class attributes and instance attributes accessible to instance method




# Class methods:


# Things to remember: 1. The 1st parameter is cls. It refers to the class.
#                     2. They are only accessible to thier class
#                     3. We use class decorator in class methods, if we don't use then it becomes the instance method. (The python interpreter things it is instance method)




class laptop:

    storage_type = "SSD"

    def __init__(self, Ram, Storage):
        self.Ram = Ram
        self.Storage = Storage 

    @classmethod   # It is the class decorater is a build in function, it changes the behaviour of the function like here the function only accessible to its class only. 
    def get_storage_type(cls):
        print(f"The storage type is {cls.storage_type}")

    def get_info(self):  #instance method
        print(f"The laptop has {self.Ram} & {self.Storage} {self.storage_type}")

laptop1 = laptop("16gb", "512gb")
laptop2 = laptop("8gb", "256gb")

laptop1.get_storage_type()



# Static methods: Things to remember: 1. They don't have any compulsary parameter like self and cls.
#                                     2. They cannot access both class attributes and instance attributes 
#                                     3. We use a decorator for static method @staticmethod to made the static method
#                                     4. We use the static method in a situation like if we want a function to calculate the discount



class laptop:

    storage_type = "SSD"

    def __init__(self, Ram, Storage):
        self.Ram = Ram
        self.Storage = Storage 

    @classmethod   # It is the class decorater is a build in function, it changes the behaviour of the function like here the function only accessible to its class only. 
    def get_storage_type(cls): #Class method
        print(f"The storage type is {cls.storage_type}")

    def get_info(self):  #instance method
        print(f"The laptop has {self.Ram} & {self.Storage} {self.storage_type}")

    @staticmethod 
    def calc_discount(price, discount): #Static method

        discount_price = price - discount * price / 100
        print(f"The final price is: {discount_price}")


laptop1 = laptop("16gb", "512gb")
laptop2 = laptop("8gb", "256gb")

laptop1.get_storage_type()

laptop1.calc_discount(40000, 10)

# _____________________________________________________________________________________________________________________________________________________________________________________________________

# Practice problem:  Product store
# Design and create an online store for products (name, price).
# Track total products being created.
# Create a static method to calculate discount on each product based on a % parameter.


class product:
    count = 0 # class attributes
       
    def __init__(self, name,price):
        self.name = name  #instance attributes
        self.price = price
        product.count+=1

    def get_info(self): #instance method 
        print("The price of {self.name} is {self.price}")

    @classmethod     
    def get_count(cls): #class method 
        print(f"The total products are created is {cls.count} ")

    @staticmethod
    def discount(price, discount): #static method

        total_discount = price - discount * price / 100
        print(f"The final price is: {total_discount}")



product1 = product("Phone", 20_000)
product2 = product("Laptop",50_000)
product3 = product("Watch", 1000)

product1.get_info()
product2.get_info()
product3.get_info()

product1.discount(product1.price, 10)
product1.discount(product2.price, 10)
product1.discount(product3.price, 10)

product.get_count()


# ___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


# 4 Main pillars of Object Oriented Programming:


# 1. Encapsulation:   Binding the data and methods/function in a single unit is called Encapsulation.

 
# Data hiding/access modifiers/access specifiers: There are three types of data hiding:

# 1. Public: data and methods are accessible to everyone. By default our data and methods are public.
# 2. protected: Data and methods are accessible to their class and theri derived class. (We can access the protected data in python but we don't do this)
# 3. private: Data and methods are accessible to only their class. (We have data mangling in private data by which if we want to access the private data we cannot able to access but if we use this [objectname._classname__variablename]  by this we can access but we don't prefer to do this)
#    If we want to give the access to the private data outside the class leagle, we can do by creating the getter and setter function.



class BankAccount:

    def __init__(self, name, balance, id):
        self.name = name  # Public
        self._balance = balance  # Protected
        self.__id = id # Private
        
    def get_ID(self): #getter function
        return self.__id
    
    def set_ID(self, new_ID): #setter function
        self.__id = new_ID
        
Person1 = BankAccount("Krishna", 20_000, 11_22_33)

print(Person1.name, Person1.get_ID())
print(Person1._balance)  # we can access protected but we prefer to not do this. (As a good programer we have to maintain the rules)

Person1.set_ID(12_13_14)
print(Person1.get_ID())

print(Person1._BankAccount__id)  #We can access private data like this but this is illegle


# _______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


# 2. Inheritance: Reusing the attrributes and methods from the  parent (base) class. 



class Employee:

    start_time = "8 AM"
    end_time = "4 PM"

    def change_time(self,new_end_time):

        self.end_time = new_end_time


class Teacher(Employee):  #Inheritance used

    def __init__(self, subject):
        self.subject = subject


class AdminStaff(Employee):

    def __init__(self, role):
        self.role = role

        
t1 = Teacher("cpp")
print(t1.subject, t1.start_time, t1.end_time)
print(t1.change_time("5 AM"))


staff1 = AdminStaff("Manager")
print(staff1.role, staff1.start_time, staff1.end_time)



# Types of Inheritance:

# 1. Single level inheritance: Reusing the data and methods from one class to another class like from parent (base) class to child (derived) class.


# 2. Multi level inheritance: Three or more classes reuses the properties and methods from the base class to derived class and their third derived class.




class Employee:

    start_time = "8 AM"
    end_time = "4 PM"

    def change_time(self,new_end_time):
        self.end_time = new_end_time


class AdminStaff(Employee):

    def __init__(self, role):
        self.role = role


class Accountant(AdminStaff):

    def __init__ (self, role, salary):  # Here the constructor things that we build an another varialbe as "role" but we want to use "role" (constructor) of parent class so we use super().AdminStaff
        super().__init__(role)
        self.salary = salary

 

acc1 = Accountant("CA", 50_000)
print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)





# 3. Multiple inheritance:  Reusing the data and methods from two or more parent (base) class to one child (derived) class.


class Teacher:

    def __init__(self, salary):
        self.salary = salary 


class Student:

    def __init__(self, gpa):

        self.gpa = gpa

 
class TA(Teacher, Student):

    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name


ta1 = TA("40_000", 8.5, "Ritika")

print(ta1.name, ta1.gpa, ta1.salary)


# _____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


# 3. Abstraction: Hiding the unnessery data and showing the important details.


 
from abc import ABC, abstractmethod

class Animal:
    @abstractmethod
    def make_sound(self):
        pass



class Lion(Animal):

    def make_sound(self):
        print("Roarrr....")

class Cat(Animal):
    
    def make_sound(self):
        print("Meoww....")


lion = Lion()
lion.make_sound()

cat = Cat()
cat.make_sound()


# ______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


# 4. Polymorphism: One function having many forms is called ploymorphism. Different functions having same name and  performing different task.

# Example:  operator overloading:  print(1 + 2, "Hello" + "Sarthak")
#                                       addition    concatenation (The "+" operator is doning both task  addition and concatenation)

# The main Two examples of the polymorphism is:

# 1. Function overriding: we use it in inheritance. one function having many forms


class employee:
    
    def designation(self):
        print("The designation is employee")

class Teacher(employee):

    def designation(self):
        print("The designation is Teacher")


t1 = Teacher()
t1.designation()


# 2. Duck Typing: we can use without inheritance. one function having many forms.


class Teacher:
    
    def designation(self):
        print("The designation is Teacher")

class AccounTant:

    def designation(self):
        print("The designation is Accountant")


t1 = Teacher()
t1.designation()

a1 = AccounTant()
a1.designation()





























