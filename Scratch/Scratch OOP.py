from __future__ import annotations

#re-entro to OOP


# work on abandonging instantiating an instance of a class if the arguments passed are not valid
# prevents the error but does nothing if that instance is called later, will still crash everything.


class dog:
   
    def __init__(self, name, breed, owner):
        if not set(map(lambda x: isinstance(x, str), [name,breed,owner])) == {True}:
            print(f"When atttempting to generate the dog {name}, not all arguments were valid. {name} was not created")
            return
        
        self.__name = name
        self.__breed = breed
        self.__owner = owner
        self.bark = lambda word="bark": print(f"{self.__name} said: {word}")

d1 = dog("roger","pug", 1)
d2 = dog("mac","doverman","Frank")
d2.bark()

# -------------- Decorators
# What are they?
# A function that takes a function. Ex: 


def prev_after(funct):
    def wrapper():
        print("before the called function")
        funct()
        print("happening after the called function")
    return wrapper

@prev_after #<-----decorator points to defined function prev_after
def hello():
    print("hello")  #<---- decorator function

hello()

#----------------Private attributes using self.__ works, but is error prone because you ahve to call the setter/getter as methods using ()
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f"{self.__name} is {self.__age}"
    

    def get_age(self):
        return self.__age
    

    def set_age(self,new_age):
        self.__age = new_age

Mike = Person("Mike",12)
print(Mike)

Mike.set_age(14)  #<------ requires calling using method and (), which is easy to forget in code and won't throw an error!  BAD
print(Mike)

# ---------------------- This works better, use @property and @method.setter to avoid calling stuff with ()
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    @property #<--------- Treating as a property, not a method
    def get_age(self):
        return self.age
    
    @get_age.setter  # <------ Setting a property, not a method
    def set_age(self,val):
        self.age = val

Bill = Person2("Bill", 23)
print(Bill)
Bill.set_age = 35   # <----- Doesn't require () because it's treated as a property and not a method!  GOOD!
print(Bill)
    

'''
Inheritance: taking attributes and passing them down to different versions of classes

'''
class animal:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color
        

class dog(animal):
    def __init__(self, name, breed, color):
        super().__init__(name,breed,color)
        self.sound = "woof"

class cat(animal):
    def __init__(self, name, breed, color):
        super().__init__(name, breed,  color)
        self.sound = "meow"
    '''Not repeating ourselves, cats and dogs are both animals'''

garfield = cat("Garfield", "Tabby", "Orange")
Odie = dog("Odie", "Dautchund", "Whilte")

print(f"cat {garfield.name} and dog {Odie.name}")

'''
Composition 
'''

class Person():
    def __init__(self,f_name,l_name,age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

    def __repr__(self):
        return f"{self.f_name} {self.l_name} is {self.age} years old"

class Father(Person):
    def __init__(self, f_name, l_name, age, children=None, spouse=None):
        super().__init__(f_name, l_name, age)
        self.child = children
        self.spouse = spouse

class Mother(Person):
    def __init__(self, f_name, l_name, age, child=None, spouse=None):
        super().__init__(f_name, l_name, age)
        self.child = child
        self.spouse = spouse

class Child(Person):
    def __init__(self, f_name, l_name, age, father, mother):
        super().__init__(f_name, l_name, age)
        self.father = father
        self.mother = mother

Dad = Father("Adam", "Cahan", 33)
Mom = Mother("Francine","Cahan", 34)
Kid = Child("Nick","Cahan",9,Dad,Mom)
Dad.spouse = Mom
Dad.child = Kid
Mom.spouse = Dad
Mom.child = Kid
Kid.father = Dad
Kid.mother = Mom
family = [Dad,Mom,Kid]
print(family)

'''
Polymorphism
'''

from abc import ABC, abstractmethod

class Shape(ABC): 
    @abstractmethod  #<----forces child classes to define this method
    def area(self):
        pass

# total = 0
# x = [[i for i in "ASDFASDFASDFASDFASDF"] for z in "ASDFASDF"]
# for key in tqdm(x):
#     total +=1
# print(total)

