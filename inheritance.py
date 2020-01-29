#Single Level Inheritance:

class Person(object): 
       
    # Constructor 
    def __init__(self, name): 
        self.name = name 
   
    # To get name 
    def getName(self): 
        return self.name 
   
    # To check if this person is employee 
    def isEmployee(self): 
        return False
   
   
# Inherited or Sub class (Note Person in bracket) 
class Employee(Person): 
   
    # Here we return true 
    def isEmployee(self): 
        return True
   
# Driver code 
emp = Person("Tony")  # An Object of Person 
print(emp.getName(), emp.isEmployee()) 
   
emp = Employee("Stark") # An Object of Employee 
print(emp.getName(), emp.isEmployee())

print()

# Multiple Inheritance  
class Base1(object): 
    def __init__(self): 
        self.str1 = "String from 1"
        print ("Base String from 1")
  
class Base2(object): 
    def __init__(self): 
        self.str2 = "String from 2"        
        print ("Base String from 2")
  
class Derived(Base1, Base2): 
    def __init__(self): 
          
        # Calling constructors of Base1 
        # and Base2 classes 
        Base1.__init__(self) 
        Base2.__init__(self) 
        print ("Hence Derived")
          
    def printing_strings(self): 
        print(self.str1, self.str2) 
         
  
ob = Derived() 
ob.printing_strings()

print()

# Multilevel Inheritance

class Base(object): 
      
    # Constructor 
    def __init__(self, name): 
        self.name = name 
  
    # To get name 
    def getName(self): 
        return self.name 
   
class Derived(Base): 
      
    # Constructor 
    def __init__(self, name, age): 
        Base.__init__(self, name) 
        self.age = age 
  
    # To get age 
    def getAge(self): 
        return self.age 
  
class FurtherDerived(Derived): 
      
    # Constructor 
    def __init__(self, name, age, address): 
        Derived.__init__(self, name, age) 
        self.address = address 
  
    # To get address 
    def getAddress(self): 
        return self.address         
  
# Driver code 
d = FurtherDerived("Albert Einstein", 50, "New York")   
print(d.getName(), d.getAge(), d.getAddress())

print()

# Hirarchial Inheritance

class Parent(object): 
      
    # Constructor 
    def __init__(self, name): 
        self.name = name 
  
    # To get name 
    def getName(self): 
        return self.name 

class Derived1(Parent): 
      
    # Constructor 
    def __init__(self, name, age): 
        Parent.__init__(self, name) 
        self.age = age 
  
    # To get name 
    def getAge(self): 
        return self.age 

class Derived2(Base): 
      
    # Constructor 
    def __init__(self, name, age): 
        Parent.__init__(self, name) 
        self.age = age 
  
    # To get name 
    def getAge(self): 
        return self.age 

# Driver Code:
d1 = Derived1("Nicola Tesla",34)
print(d1.getName(), d1.getAge())
d2 = Derived2("Michael Faraday",25)
print(d2.getName(), d2.getAge())

print()
