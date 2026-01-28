"""Now we will create two classes with one methods that is common"""

# class Mammal:
    # def eat(self):
    #     print("eat")

#     def walk(self):
#         print("walk")


# class Fish:
#     def eat(self):
#         print("eat")

#     def swim(self):
#         print("swim")

# Remember in programming we dont want to repeat same thing multiple times so we have to fix this 
# Check the following code and this is what we call inheritance
# Inheritance-> is a machanism that allows us to define the common behavior of common function in one class and inherit them in other classes


class Animal:  # Defines a common behavior of common functions in class of mammals and fish

    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

class Mammal(Animal): # Animal class act as parental/ base class and Mammal class as child / sub class
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

# lts create an mammal object+
m = Mammal()
m.eat()  # when you write the object and type dot (m.) you'll see that methods for eat does appear as well as method of walk and other methods

# inheritance doesn't  only focuses on the functions(mthonds) you can initialize attributes and they will appear on other class
# now lets go back to our code and intialize age in class Annimal and you will see it will also appear when you type "m."

print(m.age) # meaning every objcet from mammal and fish will have age 1 initialized also because they inheritated thm from Animal class

### The Object Class
"""From the class tha we created let's if we have two useful functions to see if object is an 
    instance of a class and also check class is a subclass
        fuction it tells us if object is instance of a give class"""

## note all class in python dirctly or indirectly  inherits from class called object , object class is the parental/base class for all classes in python

print(isinstance(m, Mammal)) #-> True object m is instance of mammal class
print(isinstance(m, Animal)) # -> True object m is instance of a animal class, because mammal class inherits from animal so instance of mammal class is also an animal
print(isinstance(m, object)) #-> True because mammal class inherits from aninmal class which inherits from object class

print(issubclass(Mammal, Animal)) #-> True
print(issubclass(Mammal, object)) # -> True Because mamals indirectly inherites from object class









