
# base class
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__dob = "23-04-1992"   # private member
        self.__address = "Trinity Complex"  # private member

    # if we want to access private member
    # then we need to return in the same class

    def getDob(self):
        return self.__dob

    def getAddress(self):
        return self.__address


# child class
class library(student):
    # initialization in library
    def __init__(self, name, age, fine):
        student.__init__(self, name, age)
        self.fine = fine


obj = library("Hitanshu", 33, 500)
print(f"my name is {obj.name} and age is {obj.age} and fine is {obj.fine}")
print(f"my DOB is {obj.getDob()} and address is {obj.getAddress()}")


# define private member __private_member












